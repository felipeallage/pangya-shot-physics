from dataclasses import dataclass, field

from .vector import Vector3D


@dataclass
class Ball:
    position: Vector3D = field(default_factory=lambda: Vector3D(0.0, 0.0, 0.0))
    velocity: Vector3D = field(default_factory=lambda: Vector3D(0.0, 0.0, 0.0))
    slope: Vector3D = field(default_factory=lambda: Vector3D(0.0, 1.0, 0.0))

    mass: float = 0.045926999
    diameter: float = 0.14698039

    spin: float = 0.0
    curve: float = 0.0

    rotation_spin: float = 0.0
    rotation_curve: float = 0.0

    count: int = 0
    max_height: float = 0.0
    max_height_step: int = -1
