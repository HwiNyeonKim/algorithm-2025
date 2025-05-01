import pytest

from ..최고의_집합 import solution


@pytest.mark.parametrize(
    "n, s, expected",
    [
        [2, 9, [4, 5]],
        [2, 1, [-1]],
        [2, 8, [4, 4]],
    ],
)
def test_best_set(n, s, expected):
    answer = solution(n, s)
    assert answer == expected
