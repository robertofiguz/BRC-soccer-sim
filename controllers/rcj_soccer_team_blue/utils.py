import math

def get_distance(loc_1: dict, loc_2: dict) -> float:
   return float(math.sqrt( ((loc_1['x']-loc_2['x'])**2)+((loc_1['y']-loc_2['y'])**2) ))
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

def possesses_ball(name, data, ball_angle) -> bool:
    ball_dist_threshold = 5 #todo: set threshold to reasonable value
    if (get_distance(data[name], data['ball'])<ball_dist_threshold and get_direction(ball_angle)==0):
        return True
    return False

