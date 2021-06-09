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

class Stage:
    def __init__(
        self,
        target: List[Target] = None,
        time: float = None,
    ):
        self._target = target or [],
        self._time = time or None


class Target:
    def __init__(
        self, 
        location: List[float] = None,
        move: float = None
    ):
        self._location = location or []
        self._move = move or None
    
# add keyframe logic to calculate wheel speed etc.