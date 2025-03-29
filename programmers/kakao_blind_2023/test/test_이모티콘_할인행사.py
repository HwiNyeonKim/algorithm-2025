import pytest

from ..이모티콘_할인행사 import solution


@pytest.mark.parametrize(
    "users, emoticons, expected",
    [
        [[[40, 10000], [25, 10000]], [7000, 9000], [1, 5400]],
        [
            [
                [40, 2900],
                [23, 10000],
                [11, 5200],
                [5, 5900],
                [40, 3100],
                [27, 9200],
                [32, 6900],
            ],
            [1300, 1500, 1600, 4900],
            [4, 13860],
        ],
    ],
)
def test_emoticon_discount(users, emoticons, expected):
    assert solution(users, emoticons) == expected
