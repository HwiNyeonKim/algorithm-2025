import pytest
from stack_and_queue import solution_5


@pytest.mark.parametrize(
    "prices, expected",
    [
        ([1, 2, 3, 2, 3], [4, 3, 1, 1, 0]),
    ],
)
def test_주식가격(prices, expected):
    answer = solution_5(prices)
    assert answer == expected
