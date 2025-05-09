import pytest

from ..최적의_행렬_곱셈 import solution


@pytest.mark.parametrize(
    "matrix_sizes, expected",
    [
        [[[5, 3], [3, 10], [10, 6]], 270],
        [[[10, 30], [30, 5], [5, 60], [60, 2]], 1500],
    ],
)
def test_최적의_행렬_곱셈(matrix_sizes, expected):
    answer = solution(matrix_sizes)
    assert answer == expected
