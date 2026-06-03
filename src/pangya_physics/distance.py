from .enums import DistanceType


def calculate_distance_type(distance: float) -> DistanceType:
    if distance >= 58.0:
        return DistanceType.BIGGER_OR_EQUAL_58

    if distance < 10.0:
        return DistanceType.LESS_10

    if distance < 15.0:
        return DistanceType.LESS_15

    if distance < 28.0:
        return DistanceType.LESS_28

    return DistanceType.LESS_58