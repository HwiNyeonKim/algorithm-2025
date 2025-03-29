import pytest

from ..두_원_사이의_정수_쌍 import solution


@pytest.mark.parametrize(
    "r1, r2, expected", [[2, 3, 20], [1, 4, 48], [2, 4, 40]]
)
def test_integer_pair_between_two_circles(r1, r2, expected):
    answer = solution(r1, r2)
    assert answer == expected
