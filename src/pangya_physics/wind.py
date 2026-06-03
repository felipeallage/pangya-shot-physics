from dataclasses import dataclass
import math

from .vector import Vector3D


@dataclass
class Wind:
    speed: float
    degree: float

    def to_vector(self) -> Vector3D:
        radians = math.radians(self.degree)

        return Vector3D(
            x=self.speed * math.sin(radians) * -1,
            y=0.0,
            z=self.speed * math.cos(radians),
        )
