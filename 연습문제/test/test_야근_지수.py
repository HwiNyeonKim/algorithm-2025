import pytest

from ..야근_지수 import solution


@pytest.mark.parametrize(
    "works, n, expected",
    [
        [[4, 3, 3], 4, 12],
        [[2, 1, 2], 1, 6],
        [[1, 1], 3, 0],
    ],
)
def test_night_work_index(works, n, expected):
    answer = solution(n, works)
    assert answer == expected
