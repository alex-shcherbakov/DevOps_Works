import pytest

from DevOps_Sr6.app import add, is_even


def test_add_simple():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(10, -5) == 5


@pytest.mark.parametrize("value, expected", [
    (2, True),
    (3, False),
    (10, True),
    (0, True),
    (-4, True),
    (-3, False),
])
def test_is_even(value, expected):
    assert is_even(value) == expected