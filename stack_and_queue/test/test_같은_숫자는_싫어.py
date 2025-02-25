import pytest

from ..같은_숫자는_싫어 import solution


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([1, 1, 3, 3, 0, 1, 1], [1, 3, 0, 1]),
        ([4, 4, 4, 3, 3], [4, 3]),
        ([4, 4, 4, 3, 3, 1], [4, 3, 1]),
    ],
)
def test_같은_숫자는_싫어(arr, expected):
    answer = solution(arr)

    assert answer == expected
