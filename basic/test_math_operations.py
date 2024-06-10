from math_operations import add, minus


def test_add():
    assert add(1, 2) == 3
    assert add(0, 0) == 0
    assert add(-1, 1) == 0


def test_minus():
    assert minus(1, 2) == -1
    assert minus(0, 0) == 0
    assert minus(5, 4) == 1
