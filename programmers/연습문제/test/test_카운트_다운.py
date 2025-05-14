import pytest

from ..카운트_다운 import solution


@pytest.mark.parametrize(
    "target, expected",
    [
        [21, [1, 0]],  # 7 triple
        [58, [2, 2]],  # bull + 8 single
        [61, [2, 2]],  # bull + 1 single
    ],
)
def test_카운트_다운(target, expected):
    answer = solution(target)
    assert answer == expected
