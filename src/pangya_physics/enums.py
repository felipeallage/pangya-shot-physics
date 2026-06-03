from enum import Enum


class DistanceType(Enum):
    LESS_10 = "less_10"
    LESS_15 = "less_15"
    LESS_28 = "less_28"
    LESS_58 = "less_58"
    BIGGER_OR_EQUAL_58 = "bigger_or_equal_58"


class ShotType(Enum):
    DUNK = "dunk"
    TOMAHAWK = "tomahawk"
    SPIKE = "spike"
    COBRA = "cobra"


class PowerShotType(Enum):
    NO_POWER_SHOT = "no_power_shot"
    ONE_POWER_SHOT = "one_power_shot"
    TWO_POWER_SHOT = "two_power_shot"
    ITEM_15_POWER_SHOT = "item_15_power_shot"