# rcj_soccer_player controller - ROBOT B2

# Feel free to import built-in libraries
import math
import time
# You can also import scripts that you put into the folder with controller
from rcj_soccer_robot import RCJSoccerRobot, TIME_STEP
import utils


class MyRobot2(RCJSoccerRobot):
    closer = False
    defending = False
    attacking = False
    kicking = False
    start_time = time.time()
    
    def get_time(self):
        return (time.time() - self.start_time)
        
    def get_states(self):
        self.closer = utils.am_i_closer(team = self.team, name = self.name, data = self.get_new_data())
        self.attacking = utils.am_i_attacking()
        self.posesses_ball = utils.possesses_ball(name = self.name, data = self.get_new_data())
    
    def run(self):
        while self.robot.step(TIME_STEP) != -1:
            if self.is_new_data():
                data = self.get_new_data()
                
                if self.get_time()<5: #change from time to awaiting kickoff or something that detects resets
                    utils.move_to(self, objective=self.initial_positions[self.name], robot_pos = data[self.name])
                if not self.attacking:
                    utils.move_to(self, objective=data['ball'], robot_pos=data[self.name])
                