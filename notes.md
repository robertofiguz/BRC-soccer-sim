# Soccer Simulation
It is not whether you win or lose, but how much you learn that counts! 
## RULES:
 https://github.com/RoboCupJuniorTC/soccer-rules-simulation

## Bishops Team:
 https://github.com/liunicholas/Bishops-RCJ-Soccer-Sim
 
Data received by the robot:
    
        {'B1': {'x': 0.24944748199802624, 'y': 0.35664616204739497, 'orientation': -1.5700000000000014}, 'B2': {'x': 0.3585792698975978, 'y': -0.2609904014427252, 'orientation': -1.5700000000000014}, 'B3': {'x': 0.10000000000542289, 'y': 3.081487224381361e-09, 'orientation': -1.5700000000000014}, 'Y1': {'x': -0.3141029224325791, 'y': -0.26923503496272955, 'orientation': 1.5700000000000023}, 'Y2': {'x': -0.37450724764911447, 'y': 0.36959087408364527, 'orientation': 1.5700000000000023}, 'Y3': {'x': -0.32700293848230066, 'y': -0.04884075880012318, 'orientation': 1.5700000000000023}, 'ball': {'x': 0.0, 'y': 0.0}, 'waiting_for_kickoff': False}

Data:
- same team robot position and heading
- opposite team robot position and heading
- ball position
- wether it's waiting for kickoff

Field Dimensions:
        -1.5x1.3 (without including goals)
        -center position(0,0) is in the middle of the field

## IDEAS:
- use teammates positions to pass the ball (probably unreliable but useful for long range isolated) (Move robot to end of field)
- use ball position to calculate it's heading
- predict ball direction by summing vectors by calculating every robot movement and ball movement. (robot radius, position,vector, ball position, ball vector)
- use reinforcement learning ML to teach robots to play:
  - need insight into simulation(when goals are scored, robots position and access to speeds and input variabvles into robot behaviour, robot status(if there is lack of movement), possibly oponents coordinates to to help learn to avoid them)         
- code should be modular. kicking passing. game logic etc. this way each team member can more easily and autonomously contribute to the team.
- create motion scripts:
  - steps used to perform actions on call such as kicking, passing etc. Possibly implement multiple ways to set movements example: tag "to_position:[x,y]" or "move:[L_motor_speed, R_motos_speed, time]" 
