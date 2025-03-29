import pytest

from ..무인도_여행 import solution


@pytest.mark.parametrize(
    "maps, expected",
    [
        [["X591X", "X1X5X", "X231X", "1XXX1"], [1, 1, 27]],
        [["XXX", "XXX", "XXX"], [-1]],
    ],
)
def test_uninhabited_island_travel(maps, expected):
    answer = solution(maps)
    assert answer == expected
