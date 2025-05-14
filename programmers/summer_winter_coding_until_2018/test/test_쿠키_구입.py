import pytest

from ..쿠키_구입 import solution


@pytest.mark.parametrize(
    "cookie, expected",
    [
        [[1, 1, 2, 3], 3],
        [[1, 2, 4, 5], 0],
        [[1], 0],
        [[1, 3, 2, 1], 3],
    ],
)
def test_쿠키_구입(cookie, expected):
    answer = solution(cookie)
    assert answer == expected
