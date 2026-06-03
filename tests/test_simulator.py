from pangya_physics import Ball, CLUBS, PangyaSimulator, Vector3D, Wind


def test_simulator_creation():
    ball = Ball()
    club = CLUBS["1W"]
    wind = Wind(speed=0, degree=0)

    simulator = PangyaSimulator(
        ball=ball,
        club=club,
        wind=wind,
    )

    assert simulator.club == club


def test_apply_force_has_gravity():
    ball = Ball()
    club = CLUBS["1W"]
    wind = Wind(speed=0, degree=0)

    simulator = PangyaSimulator(ball=ball, club=club, wind=wind)

    force = simulator.apply_force()

    assert force.y < 0


def test_step_updates_ball_position():
    ball = Ball(
        velocity=Vector3D(0.0, 10.0, 100.0)
    )
    club = CLUBS["1W"]
    wind = Wind(speed=0, degree=0)

    simulator = PangyaSimulator(ball=ball, club=club, wind=wind)
    simulator.step()

    assert simulator.ball.position.z > 0
    assert simulator.ball.count == 1