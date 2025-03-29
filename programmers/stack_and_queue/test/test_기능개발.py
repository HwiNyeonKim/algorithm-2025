import pytest

from ..기능개발 import solution


@pytest.mark.parametrize(
    "progresses, speeds, expected",
    [
        ([93, 30, 55], [1, 30, 5], [2, 1]),
        ([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1], [1, 3, 2]),
    ],
)
def test_기능개발(progresses, speeds, expected):
    answer = solution(progresses, speeds)
    assert answer == expected
