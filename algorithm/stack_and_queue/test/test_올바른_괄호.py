import pytest
from stack_and_queue import solution_3


@pytest.mark.parametrize(
    "s, expected",
    [
        ("()()", True),
        ("(())()", True),
        (")()(", False),
        ("(()(", False),
    ],
)
def test_올바른_괄호(s, expected):
    answer = solution_3(s)
    assert answer == expected
