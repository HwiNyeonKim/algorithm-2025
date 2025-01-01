import pytest
from sorting import solution_1


@pytest.mark.parametrize(
    "numbers, expected",
    [
        ([6, 10, 2], "6210"),
        ([3, 30, 34, 5, 9], "9534330"),
        ([0, 0, 0, 0], "0"),
    ],
)
def test_가장_큰_수(numbers, expected):
    answer = solution_1(numbers)

    assert answer == expected
