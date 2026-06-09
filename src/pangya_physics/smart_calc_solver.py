from dataclasses import dataclass

from .ball import Ball
from .club import ClubInfo
from .simulator import PangyaSimulator
from .solver import create_initial_velocity
from .wind import Wind


@dataclass
class FindPowerResult:
    power_percent: float
    desvio: float
    power_range: float
    final_distance: float
    error: float
    iterations: int
    found: bool


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
) -> FindPowerResult:
    min_percent = 0.10
    max_percent = 1.30
    feed = 0.02
    margin = 0.05
    limit_checking = 1000

    percent_shot = 1.0
    last_error = None
    found = False

    last_simulator = None
    error = 0.0

    for i in range(limit_checking):
        ball = Ball(
            velocity=create_initial_velocity(
                club=club,
                power_percent=percent_shot,
            )
        )

        simulator = PangyaSimulator(
            ball=ball,
            club=club,
            wind=wind,
        )

        error = find_height_collision(
            simulator=simulator,
            target_height=target_height,
            target_distance=target_distance,
        )

        last_simulator = simulator

        if abs(error) <= margin:
            found = True
            break

        if last_error is not None and (error > 0) != (last_error > 0):
            feed *= 0.5

        if feed < 0.000001:
            feed = 0.000001

        if error > 0:
            percent_shot += feed
        else:
            percent_shot -= feed

        percent_shot = max(min_percent, min(max_percent, percent_shot))
        last_error = error

    return FindPowerResult(
        power_percent=percent_shot,
        desvio=last_simulator.ball.position.x,
        power_range=club.power_base * percent_shot,
        final_distance=last_simulator.ball.position.z,
        error=error,
        iterations=i + 1,
        found=found,
    )