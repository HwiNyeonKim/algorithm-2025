import pytest

from ..석유_시추 import solution


@pytest.mark.parametrize(
    "land, expected",
    [
        [
            [
                [0, 0, 0, 1, 1, 1, 0, 0],
                [0, 0, 0, 0, 1, 1, 0, 0],
                [1, 1, 0, 0, 0, 1, 1, 0],
                [1, 1, 1, 0, 0, 0, 0, 0],
                [1, 1, 1, 0, 0, 0, 1, 1],
            ],
            9,
        ],
        [
            [
                [1, 0, 1, 0, 1, 1],
                [1, 0, 1, 0, 0, 0],
                [1, 0, 1, 0, 0, 1],
                [1, 0, 0, 1, 0, 0],
                [1, 0, 0, 1, 0, 1],
                [1, 0, 0, 0, 0, 0],
                [1, 1, 1, 1, 1, 1],
            ],
            16,
        ],
    ],
)
def test_석유_시추(land, expected):
    answer = solution(land)
    assert answer == expected
