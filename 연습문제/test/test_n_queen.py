import pytest

from ..n_queen import solution


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
        # (11, 2680),
        # (12, 14200),
    ],
)
def test_n_queen(n, expected):
    answer = solution(n)
    assert answer == expected
