# rcj_soccer_player controller - ROBOT B1

# Feel free to import built-in libraries
import math
import time
# You can also import scripts that you put into the folder with controller
import utils
from rcj_soccer_robot import RCJSoccerRobot, TIME_STEP

#initial positions
# todo: not adapting to field side
# a three states system probably works best: defending/attacking/get_ball vs attacking/everyhting else
class MyRobot1(RCJSoccerRobot):
    closer = False
    defending = False
    attacking = False
    defending = False
    get_ball = False
    kicking = False
    start_time = time.time()
    
    def get_time(self):
        return (time.time() - self.start_time)

    def get_states(self, data):
        self.closer = utils.am_i_closer(team = self.team, name = self.name, data = data)
        self.attacking = True
        self.defending = False
        if not utils.am_i_attacking(team = self.team, data = data):
            self.attacking = False
            self.defending = utils.am_i_defending(team = self.team, data = data)
        # if attacking you can't be defending, therefore this logic, since the verification of defending includes seeing the ball posession of all players including own team and by finding if we're attacking we can exclude the option
        self.posesses_ball = utils.possesses_ball(data[self.name], data['ball'])    
    
    def get_state(self):
        if self.attacking:
            return "attacking"
        if self.defending:
            return "defending"
        return "other"

    def run(self):
        current_state = ""
        last_state = ""
        while self.robot.step(TIME_STEP) != -1:
            if self.is_new_data():                
                data = self.get_new_data()
                self.get_states(data)
                if self.get_time()<5: #change from time to awaiting kickoff or something that detects resets
                    utils.move_to(self, objective=self.initial_positions[self.name], robot_pos = data[self.name])
                    pass
                if self.defending:
                    #utils.move_to() #move to defending position
                    pass
                    #define defending logic
                if self.attacking:
                    pass
                    #define logic
                else:
                    if utils.am_i_closer(self.team, self.name, data):
                        utils.move_to(self,data['ball'], data[self.name])
                        current_state = print(self.name+' going for the ball')
                    pass
            current_state = self.get_state()
            if current_state != last_state:
                last_state = current_state
                print(self.name + self.get_state())