import pytest

from ..베스트앨범 import solution


@pytest.mark.parametrize(
    "genres, plays, expected",
    [
        [
            ["classic", "pop", "classic", "classic", "pop"],
            [500, 600, 150, 800, 2500],
            [4, 1, 3, 0],
        ],
        [["classic"], [1000], [0]],
        [["pop", "pop", "pop"], [100, 100, 100], [0, 1]],
    ],
)
def test_베스트앨범(genres, plays, expected):
    answer = solution(genres, plays)
    assert answer == expected
