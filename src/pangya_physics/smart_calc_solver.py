from dataclasses import dataclass

from .ball import Ball
from .club import ClubInfo
from .simulator import PangyaSimulator
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
    for _ in range(max_steps):
        simulator.step()

        if simulator.ball.position.y <= target_height and simulator.ball.count > 10:
            break

    return target_distance - simulator.ball.position.z


def find_power(
    club: ClubInfo,
    wind: Wind,
    target_distance: float,
    target_height: float = 0.0,
) -> FindPowerResult:
    min_percent = 0.10
    max_percent = 1.30
    feed = 0.00006
    margin = 0.05
    limit_checking = 1000

    percent_shot = 1.0
    last_error = None
    found = False

    for i in range(limit_checking):
        ball = Ball()
        simulator = PangyaSimulator(ball=ball, club=club, wind=wind)

        # Por enquanto guardamos o percent_shot na bola/simulador depois,
        # quando confirmarmos onde a força inicial é aplicada.
        simulator.ball.power_percent = percent_shot

        error = find_height_collision(
            simulator=simulator,
            target_height=target_height,
            target_distance=target_distance,
        )

        if abs(error) <= margin:
            found = True
            break

        if last_error is not None and (error > 0) != (last_error > 0):
            feed *= 0.5

        if error > 0:
            percent_shot += feed
        else:
            percent_shot -= feed

        percent_shot = max(min_percent, min(max_percent, percent_shot))
        last_error = error

    return FindPowerResult(
        power_percent=percent_shot,
        desvio=simulator.ball.position.x,
        power_range=club.power_base * percent_shot,
        final_distance=simulator.ball.position.z,
        error=error,
        iterations=i + 1,
        found=found,
    )