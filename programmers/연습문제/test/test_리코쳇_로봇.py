import pytest

from ..리코쳇_로봇 import solution


@pytest.mark.parametrize(
    "board, expected",
    [
        [["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."], 7],
        [[".D.R", "....", ".G..", "...D"], -1],
    ],
)
def test_ricochet_robot(board, expected):
    answer = solution(board)
    assert answer == expected
