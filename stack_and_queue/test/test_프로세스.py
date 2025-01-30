import pytest

from stack_and_queue import solution_4


@pytest.mark.parametrize(
    "priorities, location, expected",
    [([2, 1, 3, 2], 2, 1), ([1, 1, 9, 1, 1, 1], 0, 5)],
)
def test_프로세스_1(priorities, location, expected):
    answer = solution_4(priorities, location)

    assert answer == expected
