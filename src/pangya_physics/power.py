from dataclasses import dataclass

from .enums import PowerShotType


@dataclass(frozen=True)
class ExtraPower:
    auxpart: float = 0.0
    mascot: float = 0.0
    card: float = 0.0

    def total(self) -> float:
        return self.auxpart + self.mascot + self.card


@dataclass(frozen=True)
class PlayerPower:
    pwr: float
    extra: ExtraPower


def get_power_shot_bonus(power_shot: PowerShotType) -> float:

    if power_shot == PowerShotType.ONE_POWER_SHOT:
        return 10.0

    if power_shot == PowerShotType.TWO_POWER_SHOT:
        return 20.0

    if power_shot == PowerShotType.ITEM_15_POWER_SHOT:
        return 15.0

    return 0.0