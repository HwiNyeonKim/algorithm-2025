import pytest

from ..선입_선출_스케줄링 import solution


@pytest.mark.parametrize(
    "n, cores, expected",
    [
        [6, [1, 2, 3], 2],
        [6, [3, 1, 2], 3],
        [1, [1, 2, 3], 1],
        [3, [2, 3, 5], 3],
        [7, [2, 2, 2], 1],
        [10, [1, 3, 4], 1],
        [15, [2, 4, 6, 7], 2],
    ],
)
def test_선입_선출_스케줄링(n, cores, expected):
    answer = solution(n, cores)
    assert answer == expected
