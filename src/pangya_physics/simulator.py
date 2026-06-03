from dataclasses import dataclass

from .ball import Ball
from .club import ClubInfo
from .constants import (
    GRAVITY,
    STEP_TIME,
    MAGNUS_FACTOR,
    CURVE_FORCE_FACTOR,
    SPIN_FORCE_FACTOR,
)
from .vector import Vector3D
from .wind import Wind


@dataclass
class PangyaSimulator:
    ball: Ball
    club: ClubInfo
    wind: Wind

    gravity: float = GRAVITY

    def apply_force(self) -> Vector3D:
        force = Vector3D(0.0, 0.0, 0.0)

        if self.ball.rotation_curve != 0:
            curve_vector = Vector3D(
                self.ball.velocity.z * -1.0,
                0.0,
                self.ball.velocity.x,
            ).normalize()

            curve_vector = curve_vector * (
                CURVE_FORCE_FACTOR
                * self.ball.rotation_curve
                * self.club.rotation_curve
            )

            force = force + curve_vector

        wind_force = self.wind.to_vector() * STEP_TIME
        force = force + wind_force

        gravity_force = Vector3D(
            0.0,
            -self.gravity * self.ball.mass,
            0.0,
        )
        force = force + gravity_force

        if self.ball.rotation_spin != 0:
            force.y += (
                self.club.rotation_spin
                * SPIN_FORCE_FACTOR
                * self.ball.rotation_spin
            )

        drag = self.ball.velocity * (
            self.ball.velocity.length() * MAGNUS_FACTOR
        )

        force = force - drag

        return force

    def step(self, delta_time: float = STEP_TIME) -> Ball:
        acceleration = self.apply_force() / self.ball.mass

        self.ball.velocity = self.ball.velocity + (acceleration * delta_time)
        self.ball.position = self.ball.position + (self.ball.velocity * delta_time)

        self.ball.count += 1

        if self.ball.velocity.y < 0 and self.ball.max_height_step < 0:
            self.ball.max_height = self.ball.position.y
            self.ball.max_height_step = self.ball.count

        return self.ball