import pytest

from ..완전범죄 import solution


@pytest.mark.parametrize(
    "info, n, m, expected",
    [
        [[[1, 2], [2, 3], [2, 1]], 4, 4, 2],
        [[[1, 2], [2, 3], [2, 1]], 1, 7, 0],
        [[[3, 3], [3, 3]], 7, 1, 6],
        [[[3, 3], [3, 3]], 6, 1, -1],
    ],
)
def test_perfect_crime(info, n, m, expected):
    answer = solution(info, n, m)
    assert answer == expected
