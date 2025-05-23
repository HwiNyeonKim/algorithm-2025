import pytest

from ..largest_three_same_digit_number import largest_good_integer


@pytest.mark.parametrize(
    "num, expected",
    [
        ["6777133339", "777"],
        ["2300019", "000"],
        ["42352338", ""],
    ],
)
def test_largest_three_same_digit_number(num, expected):
    answer = largest_good_integer(num)
    assert answer == expected
