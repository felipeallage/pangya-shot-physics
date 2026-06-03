from pangya_physics import CLUBS, Wind, find_velocity_for_distance


def test_find_velocity_for_distance():
    club = CLUBS["1W"]
    wind = Wind(speed=0, degree=0)

    result = find_velocity_for_distance(
        target_distance=200,
        club=club,
        wind=wind,
    )

    assert abs(result.error) <= 1.0
    assert result.velocity_z > 0