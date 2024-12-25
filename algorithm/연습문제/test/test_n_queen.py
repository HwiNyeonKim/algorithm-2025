import pytest
from 연습문제 import solution_1


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, 1),
        (2, 0),
        (3, 0),
        (4, 2),
        (5, 10),
        (6, 4),
        (7, 40),
        (8, 92),
        (9, 352),
        (10, 724),
        (11, 2680),
        (12, 14200),
    ],
)
def test_n_queen(n, expected):
    answer = solution_1(n)
    assert answer == expected
