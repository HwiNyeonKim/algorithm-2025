import pytest

from ..largest_number import largest_numer


@pytest.mark.parametrize(
    "nums, expected",
    [
        [[10, 2], "210"],
        [[3, 30, 34, 5, 9], "9534330"],
        [[111111121, 11111112], "11111112111111121"],
        [[0, 0], "0"],
    ],
)
def test_largest_number(nums, expected):
    answer = largest_numer(nums)
    assert answer == expected
