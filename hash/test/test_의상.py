import pytest

from hash import solution_2


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
    answer = solution_2(clothes)
    assert answer == expected
