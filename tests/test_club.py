from pangya_physics.club import CLUBS


def test_club_exists():

    club = CLUBS["1W"]

    assert club.power_factor > 0
    assert club.power_base > 0