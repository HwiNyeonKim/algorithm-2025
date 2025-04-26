import pytest

from ..합승_택시_요금 import solution


@pytest.mark.parametrize(
    "n, s, a, b, fares, expected",
    [
        [
            6,
            4,
            6,
            2,
            [
                [4, 1, 10],
                [3, 5, 24],
                [5, 6, 2],
                [3, 1, 41],
                [5, 1, 24],
                [4, 6, 50],
                [2, 4, 66],
                [2, 3, 22],
                [1, 6, 25],
            ],
            82,
        ],
        [
            7,
            3,
            4,
            1,
            [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]],
            14,
        ],
        [
            6,
            4,
            5,
            6,
            [
                [2, 6, 6],
                [6, 3, 7],
                [4, 6, 7],
                [6, 5, 11],
                [2, 5, 12],
                [5, 3, 20],
                [2, 4, 8],
                [4, 3, 9],
            ],
            18,
        ],
    ],
)
def test_합승_택시_요금(n, s, a, b, fares, expected):
    answer = solution(n, s, a, b, fares)
    assert answer == expected
