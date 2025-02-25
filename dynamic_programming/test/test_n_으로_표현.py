import pytest

from ..n_으로_표현 import solution


@pytest.mark.parametrize(
    "n, number, expected",
    [
        [5, 12, 4],
        [2, 11, 3],
        [7, 7, 1],
    ],
)
def test_express_with_n(n, number, expected):
    answer = solution(n, number)
    assert answer == expected
