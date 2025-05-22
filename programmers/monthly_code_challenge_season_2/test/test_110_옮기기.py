import pytest

from ..moving_110 import move_110, solution


@pytest.mark.parametrize(
    "s, expected",
    [
        ["1110", "1101"],
        ["100111100", "100110110"],
        ["0111111010", "0110110111"],
        ["0001110", "0001101"],
    ],
)
def test_move_110(s, expected):
    assert move_110(s) == expected


def test_110_옮기기():
    s = ["1110", "100111100", "0111111010"]
    expected = ["1101", "100110110", "0110110111"]
    assert solution(s) == expected
