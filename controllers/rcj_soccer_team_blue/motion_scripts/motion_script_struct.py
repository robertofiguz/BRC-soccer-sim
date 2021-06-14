from typing import List


class motion_script:
    def __init__(self, name: str, stages: Optional[List[Stage]] = None):
        self._name = name
        self._stages = stages or []

    @property
    def name(self):
        return self._name

    def add_stage(self, stage: Stage):
        self._stages.append(stage)

    @property
    def stages(self):
        return self._stages

    def move_type(self):
        if self._move:
            return "move"
        return "location"
    
    def run(self):
        #should I load the script name or the variable containing the script class(MotionScript)
        #I dont need to pass in the cscript name or content since the class contains it and the function run can access the variables by self.
        for i in Stage:
            for i in target:
                #calculate speed * constant calibrating speed to movement time and for x seconds set motors speed to x
                #speed normalization consists in the process of converting speed to a variable that when multiplied by the distance will give us the time it's moving at defined speed
                time = (speed / distance) * constant
                #how will it set motor speed for required time? return and handled on the other side?  would rather handle inside  this class

class Stage:
    def __init__(
        self,
        target: List[Target] = None,
        time: float = None,
    ):
        self._target = target or [],
        self._time = time or None
        #todo: is tme the best measurement taking in account how multiple movements in a tage and a single timeframe involve complex possibly unecessary calculations??
        #possibly speed?


class Target:
    def __init__(
        self, 
        location: List[float] = None,
        move: float = None,
        speed: float = 1, #set a range? 0-5?
    ):
        self._location = location or []
        self._move = move or None
        self._speed = speed or 1
    
# add keyframe logic to calculate wheel speed etc.