from __future__ import annotations

from dataclasses import dataclass
import math


@dataclass
class Vector3D:
    x: float
    y: float
    z: float

    def length(self) -> float:
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def normalize(self) -> "Vector3D":
        length = self.length()

        if length == 0:
            return Vector3D(0.0, 0.0, 0.0)

        return self / length

    def cross(self, other: "Vector3D") -> "Vector3D":
        return Vector3D(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x,
        )

    def __add__(self, other: "Vector3D") -> "Vector3D":
        return Vector3D(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z,
        )

    def __sub__(self, other: "Vector3D") -> "Vector3D":
        return Vector3D(
            self.x - other.x,
            self.y - other.y,
            self.z - other.z,
        )

    def __mul__(self, scalar: float) -> "Vector3D":
        return Vector3D(
            self.x * scalar,
            self.y * scalar,
            self.z * scalar,
        )

    def __truediv__(self, scalar: float) -> "Vector3D":
        if scalar == 0:
            return Vector3D(0.0, 0.0, 0.0)

        return Vector3D(
            self.x / scalar,
            self.y / scalar,
            self.z / scalar,
        )
