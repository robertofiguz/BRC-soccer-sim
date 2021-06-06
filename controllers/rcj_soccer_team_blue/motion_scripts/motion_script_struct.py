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
    #check how this ^ is used
    @property
    def stages(self):
        return self._stages

class Stage:
    def __init__(
        self,
        
        speed_mode: bool = True,
        target: List[float] = None,
        time: float = None,
    ):
    #set target to new class
        self._speed_mode = speed_mode,
        self._target = target or [],
        self._time = time or None

    def add_keyframe(self, keyframe: KeyFrame):
        self._keyframes.append(KeyFrame)

    @property
    def keyframes(self):
        return self._keyframes

class KeyFrame:
    def __init__(
            self, move_cycles: int, target_position: dict, pause_cycles: int = 0
    ):
        #todo: add target position/movement(speed)
        self._pause_cycles = pause_cycles
        self._move_cycles = move_cycles
        self._target_position = target_position
        
    @property
    def pause_cycles(self):
        return self._pause_cycles

    @property
    def move_cycles(self):
        return self._move_cycles

    @property
    def target_angles(self):
        return self._target_position
