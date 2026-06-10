from dataclasses import dataclass
import math

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


@dataclass
class FindPowerResult:
    power_percent: float
    desvio: float
    power_range: float
    final_distance: float
    error: float
    iterations: int
    found: bool
    reachable: bool


def create_initial_velocity(club: ClubInfo, power_percent: float) -> Vector3D:
    initial_power = club.power_factor * power_percent
    angle = club.degree_rad()

    velocity_y = initial_power * math.sin(angle)
    velocity_z = initial_power * math.cos(angle)

    return Vector3D(0.0, velocity_y, velocity_z)


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


def find_height_collision(
    simulator: PangyaSimulator,
    target_height: float,
    target_distance: float,
    max_steps: int = 3000,
) -> float:
    previous_y = simulator.ball.position.y

    for _ in range(max_steps):
        simulator.step()

        current_y = simulator.ball.position.y
        current_z = simulator.ball.position.z

        crossed_target_height = (
            previous_y >= target_height
            and current_y <= target_height
            and simulator.ball.velocity.y < 0
            and simulator.ball.count > 10
        )

        if crossed_target_height:
            return target_distance - current_z

        previous_y = current_y

    return target_distance - simulator.ball.position.z

def find_power(
    club: ClubInfo,
    wind: Wind,
    target_distance: float,
    target_height: float = 0.0,
    tolerance: float = 0.5,
    max_iterations: int = 60,
) -> FindPowerResult:
    min_percent = 0.10
    max_percent = 1.30

    low = min_percent
    high = max_percent
    best_result = None

    for i in range(max_iterations):
        power_percent = (low + high) / 2

        ball = Ball(
            velocity=create_initial_velocity(
                club=club,
                power_percent=power_percent,
            )
        )

        simulator = PangyaSimulator(ball=ball, club=club, wind=wind)

        error = find_height_collision(
            simulator=simulator,
            target_height=target_height,
            target_distance=target_distance,
        )

        best_result = FindPowerResult(
            power_percent=power_percent,
            desvio=simulator.ball.position.x,
            power_range=club.power_base * power_percent,
            final_distance=simulator.ball.position.z,
            error=error,
            iterations=i + 1,
            found=abs(error) <= tolerance,
            reachable=True,
        )

        if abs(error) <= tolerance:
            return best_result

        if error > 0:
            low = power_percent
        else:
            high = power_percent

    return best_result
