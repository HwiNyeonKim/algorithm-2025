import pytest

from ..등대 import solution


@pytest.mark.parametrize(
    "n, lighthouse, expected",
    [
        [8, [[1, 2], [1, 3], [1, 4], [1, 5], [5, 6], [5, 7], [5, 8]], 2],
        [
            10,
            [
                [4, 1],
                [5, 1],
                [5, 6],
                [7, 6],
                [1, 2],
                [1, 3],
                [6, 8],
                [2, 9],
                [9, 10],
            ],
            3,
        ],
    ],
)
def test_등대(n, lighthouse, expected):
    answer = solution(n, lighthouse)
    assert answer == expected
