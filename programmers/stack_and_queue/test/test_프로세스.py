import pytest

from ..프로세스 import solution


@pytest.mark.parametrize(
    "priorities, location, expected",
    [([2, 1, 3, 2], 2, 1), ([1, 1, 9, 1, 1, 1], 0, 5)],
)
def test_프로세스_1(priorities, location, expected):
    answer = solution(priorities, location)

    assert answer == expected
