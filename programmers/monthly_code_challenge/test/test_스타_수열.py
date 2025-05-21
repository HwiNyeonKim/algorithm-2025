import pytest

from ..스타_수열 import solution


@pytest.mark.parametrize(
    "a, expected",
    [
        [[0], 0],
        [[5, 2, 3, 3, 5, 3], 4],
        [[0, 3, 3, 0, 7, 2, 0, 2, 2, 0], 8],
        [[1, 2, 1, 3, 1, 4, 1, 5], 8],
        [[1, 2, 3, 1, 1, 4, 5, 1], 8],
    ],
)
def test_스타_수열(a, expected):
    answer = solution(a)
    assert answer == expected
