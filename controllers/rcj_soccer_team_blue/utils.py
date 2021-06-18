import math


def __getAngle(objective: dict, robot_pos: dict):

        robot_angle: float = robot_pos['orientation']

        # Get the angle between the robot and the ball
        angle = math.atan2(
            objective['y'] - robot_pos['y'],
            objective['x'] - robot_pos['x'],
        )

        if angle < 0:
            angle = 2 * math.pi + angle

        if robot_angle < 0:
            robot_angle = 2 * math.pi + robot_angle

        robot_ball_angle = math.degrees(angle + robot_angle)

        # Axis Z is forward
        # TODO: change the robot's orientation so that X axis means forward
        robot_ball_angle -= 90
        if robot_ball_angle > 360:
            robot_ball_angle -= 360

        return robot_ball_angle, robot_angle

def move_to(self, objective: dict, robot_pos: dict):

    direction = get_direction(__getAngle(objective = objective, robot_pos=robot_pos)[0])
    if direction == 0:
        left_speed = -5
        right_speed = -5
    else:
        left_speed = 4
        right_speed = -4

    self.left_motor.setVelocity(left_speed)
    self.right_motor.setVelocity(right_speed)

def get_distance(loc_1: dict, loc_2: dict) -> float:
   return float(math.sqrt(((loc_1['x']-loc_2['x'])**2)+((loc_1['y']-loc_2['y'])**2) ))
def get_direction(ball_angle: float) -> int:
    """Get direction to navigate robot to face the ball

    Args:
        ball_angle (float): Angle between the ball and the robot

    Returns:
        int: 0 = forward, -1 = right, 1 = left
    """
    if ball_angle >= 345 or ball_angle <= 15:
        return 0
    return -1 if ball_angle < 180 else 1


def am_i_attacking(team, data) -> bool:
    players = [data[team+str(1)], data[team+str(2)], data[team+str(3)]]
    for i in players:
        if possesses_ball(i, data['ball']):
            return True
    return False

def am_i_defending(team, data) -> bool:
    players = data.copy()
    del players['ball']
    del players['waiting_for_kickoff']
    for key in players:
        if possesses_ball(players[key], data['ball']):
            return True
    return False


def am_i_closer(team, name, data) -> bool:
    
    player_1 = data[team+str(1)]
    player_2 = data[team+str(2)]
    player_3 = data[team+str(3)]
    ball = data['ball']

    distances = {
        team+str(1) : get_distance(player_1, ball),
        team+str(2) : get_distance(player_2, ball),
        team+str(3) : get_distance(player_3, ball),
    }

    if distances[name]>=max(distances.values()):
        return True
    return False

def possesses_ball(player, ball) -> bool:
    ball_dist_threshold = 0.1 #todo: set threshold to reasonable value
    if (get_distance(player, ball)<ball_dist_threshold ):
        return True
    return False

