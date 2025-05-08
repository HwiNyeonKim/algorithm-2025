import pytest

from ..퍼즐_조각_채우기 import solution


@pytest.mark.parametrize(
    "game_board, table, expected",
    [
        [
            [
                [1, 1, 0, 0, 1, 0],
                [0, 0, 1, 0, 1, 0],
                [0, 1, 1, 0, 0, 1],
                [1, 1, 0, 1, 1, 1],
                [1, 0, 0, 0, 1, 0],
                [0, 1, 1, 1, 0, 0],
            ],
            [
                [1, 0, 0, 1, 1, 0],
                [1, 0, 1, 0, 1, 0],
                [0, 1, 1, 0, 1, 1],
                [0, 0, 1, 0, 0, 0],
                [1, 1, 0, 1, 1, 0],
                [0, 1, 0, 0, 0, 0],
            ],
            14,
        ],
        [
            [[0, 0, 0], [1, 1, 0], [1, 1, 1]],
            [[1, 1, 1], [1, 0, 0], [0, 0, 0]],
            0,
        ],
    ],
)
def test_퍼즐_조각_채우기(game_board, table, expected):
    answer = solution(game_board, table)
    assert answer == expected
