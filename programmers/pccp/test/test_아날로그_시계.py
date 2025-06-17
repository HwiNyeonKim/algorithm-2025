import pytest

from ..아날로그_시계 import solution


@pytest.mark.parametrize(
    "h1, m1, s1, h2, m2, s2, expected",
    [
        (0, 5, 30, 0, 7, 0, 2),
        (12, 0, 0, 12, 0, 30, 1),
        (0, 6, 1, 0, 6, 6, 0),
        (11, 59, 58, 12, 0, 0, 1),
        (11, 58, 59, 11, 59, 0, 1),
        (0, 0, 0, 23, 59, 59, 2852),
        (0, 0, 0, 23, 0, 0, 2735),
        (0, 0, 0, 22, 59, 59, 2734),
    ],
)
def test_아날로그_시계(h1, m1, s1, h2, m2, s2, expected):
    assert solution(h1, m1, s1, h2, m2, s2) == expected
