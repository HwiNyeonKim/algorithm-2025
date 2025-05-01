import pytest

from ..아이템_줍기 import solution


@pytest.mark.parametrize(
    "rectangle, characterX, characterY, itemX, itemY, expected",
    [
        (
            [[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]],
            1,
            3,
            7,
            8,
            17,
        ),
        (
            [[1, 1, 8, 4], [2, 2, 4, 9], [3, 6, 9, 8], [6, 3, 7, 7]],
            9,
            7,
            6,
            1,
            11,
        ),
        ([[1, 1, 5, 7]], 1, 1, 4, 7, 9),
        ([[2, 1, 7, 5], [6, 4, 10, 10]], 3, 1, 7, 10, 15),
        ([[2, 2, 5, 5], [1, 3, 6, 4], [3, 1, 4, 6]], 1, 4, 6, 3, 10),
    ],
)
def test_item_looting(
    rectangle, characterX, characterY, itemX, itemY, expected
):
    answer = solution(rectangle, characterX, characterY, itemX, itemY)
    assert answer == expected
