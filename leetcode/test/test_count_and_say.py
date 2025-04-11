import pytest

from ..count_and_say import count_and_say


@pytest.mark.parametrize(
    "n, expected",
    [
        [4, "1211"],
        [3, "21"],
        [2, "11"],
        [1, "1"],
    ],
)
def test_count_and_say(n, expected):
    answer = count_and_say(n)
    assert answer == expected
