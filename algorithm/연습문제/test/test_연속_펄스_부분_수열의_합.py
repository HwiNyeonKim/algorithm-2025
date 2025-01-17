import pytest

from algorithm.연습문제 import solution_4


@pytest.mark.parametrize(
    "sequence, expected",
    [
        ([2, 3, -6, 1, 3, -1, 2, 4], 10),
        ([1000, 1, 1000, 1, 1000, 1, 1000], 3997),
    ],
)
def test_연속_펄스_부분_수열의_합(sequence, expected):
    assert solution_4(sequence) == expected
