from pangya_physics import CLUBS, Wind, find_power


def test_find_power_reaches_target_distance():
    club = CLUBS["1W"]
    wind = Wind(speed=0, degree=0)

    result = find_power(
        club=club,
        wind=wind,
        target_distance=200,
        target_height=0,
    )

    assert abs(result.error) <= 1.0
    assert 0.10 <= result.power_percent <= 1.30
    assert result.final_distance > 0