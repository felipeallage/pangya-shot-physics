from dataclasses import dataclass

from .ball import Ball
from .club import ClubInfo
from .simulator import PangyaSimulator
from .vector import Vector3D
from .wind import Wind


@dataclass
class SolverResult:
    target_distance: float
    velocity_z: float
    final_distance: float
    error: float


def simulate_distance(
    club: ClubInfo,
    wind: Wind,
    velocity_y: float,
    velocity_z: float,
    max_steps: int = 500,
) -> float:
    ball = Ball(
        velocity=Vector3D(0.0, velocity_y, velocity_z),
    )

    simulator = PangyaSimulator(ball=ball, club=club, wind=wind)

    for _ in range(max_steps):
        simulator.step()

        if simulator.ball.position.y < 0 and simulator.ball.count > 10:
            break

    return simulator.ball.position.z


def find_velocity_for_distance(
    target_distance: float,
    club: ClubInfo,
    wind: Wind,
    velocity_y: float = 40.0,
    min_velocity_z: float = 50.0,
    max_velocity_z: float = 400.0,
    tolerance: float = 0.5,
    max_iterations: int = 50,
) -> SolverResult:
    low = min_velocity_z
    high = max_velocity_z

    best_result = None

    for _ in range(max_iterations):
        mid = (low + high) / 2

        final_distance = simulate_distance(
            club=club,
            wind=wind,
            velocity_y=velocity_y,
            velocity_z=mid,
        )

        error = final_distance - target_distance

        best_result = SolverResult(
            target_distance=target_distance,
            velocity_z=mid,
            final_distance=final_distance,
            error=error,
        )

        if abs(error) <= tolerance:
            return best_result

        if final_distance < target_distance:
            low = mid
        else:
            high = mid

    return best_result
    ...