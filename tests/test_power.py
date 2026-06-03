from pangya_physics.enums import PowerShotType
from pangya_physics.power import get_power_shot_bonus


def test_power_shot_none():
    assert get_power_shot_bonus(
        PowerShotType.NO_POWER_SHOT
    ) == 0.0


def test_power_shot_one():
    assert get_power_shot_bonus(
        PowerShotType.ONE_POWER_SHOT
    ) == 10.0


def test_power_shot_two():
    assert get_power_shot_bonus(
        PowerShotType.TWO_POWER_SHOT
    ) == 20.0