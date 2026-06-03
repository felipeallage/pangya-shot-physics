from pangya_physics.vector import Vector3D


def test_vector_length():
    vector = Vector3D(3, 4, 0)

    assert vector.length() == 5


def test_vector_addition():
    a = Vector3D(1, 2, 3)
    b = Vector3D(4, 5, 6)

    result = a + b

    assert result.x == 5
    assert result.y == 7
    assert result.z == 9


def test_vector_cross_product():
    a = Vector3D(1, 0, 0)
    b = Vector3D(0, 1, 0)

    result = a.cross(b)

    assert result.x == 0
    assert result.y == 0
    assert result.z == 1
