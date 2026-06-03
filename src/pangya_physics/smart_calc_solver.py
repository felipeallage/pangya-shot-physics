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
    # Placeholder funcional.
    # Depois vamos substituir por uma versão fiel à Smart Calc.
    ball = Ball()
    simulator = PangyaSimulator(ball=ball, club=club, wind=wind)

    error = find_height_collision(
        simulator=simulator,
        target_height=target_height,
        target_distance=target_distance,
    )

    return FindPowerResult(
        power_percent=0.0,
        desvio=0.0,
        power_range=0.0,
        final_distance=simulator.ball.position.z,
        error=error,
        iterations=simulator.ball.count,
        found=False,
    )