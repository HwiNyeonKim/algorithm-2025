import pytest

from ..의상 import solution


@pytest.mark.parametrize(
    "clothes, expected",
    [
        [
            [
                ["yellow_hat", "headgear"],
                ["blue_sunglasses", "eyewear"],
                ["green_turban", "headgear"],
            ],
            5,
        ],
        [
            [
                ["crow_mask", "face"],
                ["blue_sunglasses", "face"],
                ["smoky_makeup", "face"],
            ],
            3,
        ],
    ],
)
def test_의상(clothes, expected):
    answer = solution(clothes)
    assert answer == expected
