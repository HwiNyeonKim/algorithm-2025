import pytest

from ..올바른_괄호의_갯수 import solution


@pytest.mark.parametrize(
    "n, expected",
    [
        [2, 2],
        [3, 5],
    ],
)
def test_올바른_괄호의_갯수(n, expected):
    answer = solution(n)
    assert answer == expected
