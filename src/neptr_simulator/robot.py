import math
from dataclasses import dataclass

@dataclass
class Robot:
    #position
    x: float = 0.0
    y: float = 0.0
    theta: float = 0.0

#dimensions
wheel_radius: float = 0.05
wheel_base: float = 0.30

def step(
        self,
        left_wheel_speed: float,
        right_wheel_speed: float,
        dt: float,
)
