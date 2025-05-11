import pytest

from ..기지국_설치 import solution


@pytest.mark.parametrize(
    "n, stations, w, expected",
    [
        [11, [4, 11], 1, 3],
        [16, [9], 2, 3],
        [7, [3, 4, 5], 1, 2],
    ]
)
def test_기지국_설치(n, stations, w, expected):
    answer = solution(n, stations, w)
    assert answer == expected
