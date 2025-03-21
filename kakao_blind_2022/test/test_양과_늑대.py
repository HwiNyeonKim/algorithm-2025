import pytest

from ..양과_늑대 import solution


@pytest.mark.parametrize(
    "info, edges, expected",
    [
        [
            [0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
            [
                [0, 1],
                [1, 2],
                [1, 4],
                [0, 8],
                [8, 7],
                [9, 10],
                [9, 11],
                [4, 3],
                [6, 5],
                [4, 6],
                [8, 9],
            ],
            5,
        ],
        [
            [0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0],
            [
                [0, 1],
                [0, 2],
                [1, 3],
                [1, 4],
                [2, 5],
                [2, 6],
                [3, 7],
                [4, 8],
                [6, 9],
                [9, 10],
            ],
            5,
        ],
    ],
)
def test_sheeps_and_wolves(info, edges, expected):
    assert solution(info, edges) == expected
