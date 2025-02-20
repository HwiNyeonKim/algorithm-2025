import pytest

from dynamic_programming import express_with_n


@pytest.mark.parametrize(
    "n, number, expected",
    [
        [5, 12, 4],
        [2, 11, 3],
    ],
)
def test_express_with_n(n, number, expected):
    answer = express_with_n(n, number)
    assert answer == expected
