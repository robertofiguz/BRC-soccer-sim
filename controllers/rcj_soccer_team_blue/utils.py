import math


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
        team+str(1) : math.sqrt( ((player_1['x']-ball['x'])**2)+((player_1['y']-ball['y'])**2) ),
        team+str(2) : math.sqrt( ((player_2['x']-ball['x'])**2)+((player_2['y']-ball['y'])**2) ),
        team+str(3) : math.sqrt( ((player_3['x']-ball['x'])**2)+((player_3['y']-ball['y'])**2) ),
    }

    if distances[name]>=max(distances.values()):
        return True
    return False
