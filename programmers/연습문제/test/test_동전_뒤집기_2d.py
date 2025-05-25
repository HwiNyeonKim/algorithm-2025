import pytest

from ..동전_뒤집기_2d import solution


@pytest.mark.parametrize(
    "beginning, target, expected",
    [
        [
            [
                [0, 1, 0, 0, 0],
                [1, 0, 1, 0, 1],
                [0, 1, 1, 1, 0],
                [1, 0, 1, 1, 0],
                [0, 1, 0, 1, 0],
            ],
            [
                [0, 0, 0, 1, 1],
                [0, 0, 0, 0, 1],
                [0, 0, 1, 0, 1],
                [0, 0, 0, 1, 0],
                [0, 0, 0, 0, 1],
            ],
            5,
        ],
        [
            [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
            [[1, 0, 1], [0, 0, 0], [0, 0, 0]],
            -1,
        ],
    ],
)
def test_동전_뒤집기_2d(beginning, target, expected):
    answer = solution(beginning, target)
    assert answer == expected
