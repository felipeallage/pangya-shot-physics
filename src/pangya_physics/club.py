from dataclasses import dataclass
from enum import Enum
import math


class ClubType(Enum):
    WOOD = "wood"
    IRON = "iron"
    WEDGE = "wedge"
    PUTTER = "putter"


@dataclass(frozen=True)
class ClubInfo:
    club_type: ClubType
    rotation_spin: float
    rotation_curve: float
    power_factor: float
    degree: float
    power_base: float

    def degree_rad(self) -> float:
        return math.radians(self.degree)


CLUBS = {
    "1W": ClubInfo(ClubType.WOOD, 0.55, 1.61, 236.0, 10.0, 230.0),
    "2W": ClubInfo(ClubType.WOOD, 0.50, 1.41, 204.0, 13.0, 210.0),
    "3W": ClubInfo(ClubType.WOOD, 0.45, 1.26, 176.0, 16.0, 190.0),
    "2I": ClubInfo(ClubType.IRON, 0.45, 1.07, 161.0, 20.0, 180.0),
    "3I": ClubInfo(ClubType.IRON, 0.45, 0.95, 149.0, 24.0, 170.0),
    "4I": ClubInfo(ClubType.IRON, 0.45, 0.83, 139.0, 28.0, 160.0),
    "5I": ClubInfo(ClubType.IRON, 0.45, 0.73, 131.0, 32.0, 150.0),
    "6I": ClubInfo(ClubType.IRON, 0.41, 0.67, 124.0, 36.0, 140.0),
    "7I": ClubInfo(ClubType.IRON, 0.36, 0.61, 118.0, 40.0, 130.0),
    "8I": ClubInfo(ClubType.IRON, 0.30, 0.57, 114.0, 44.0, 120.0),
    "9I": ClubInfo(ClubType.IRON, 0.25, 0.53, 110.0, 48.0, 110.0),
    "PW": ClubInfo(ClubType.WEDGE, 0.18, 0.49, 107.0, 52.0, 100.0),
    "SW": ClubInfo(ClubType.WEDGE, 0.17, 0.42, 93.0, 56.0, 80.0),
}
