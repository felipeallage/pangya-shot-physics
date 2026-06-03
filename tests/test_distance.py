from pangya_physics.distance import calculate_distance_type
from pangya_physics.enums import DistanceType


def test_distance_less_10():
    assert calculate_distance_type(5) == DistanceType.LESS_10


def test_distance_less_15():
    assert calculate_distance_type(12) == DistanceType.LESS_15


def test_distance_less_28():
    assert calculate_distance_type(20) == DistanceType.LESS_28


def test_distance_less_58():
    assert calculate_distance_type(40) == DistanceType.LESS_58


def test_distance_greater_58():
    assert calculate_distance_type(100) == DistanceType.BIGGER_OR_EQUAL_58