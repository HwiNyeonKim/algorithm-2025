import pytest

from ..올바른_괄호 import solution


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
    answer = solution(s)
    assert answer == expected
