import pytest

from ..봉인된_주문 import solution


@pytest.mark.parametrize(
    "n, bans, expected",
    [
        [30, ["d", "e", "bb", "aa", "ae"], "ah"],
        [
            7388,
            ["gqk", "kdn", "jxj", "jxi", "fug", "jxg", "ewq", "len", "bhc"],
            "jxk",
        ],
    ],
)
def test_sealed_spell(n, bans, expected):
    answer = solution(n, bans)
    assert answer == expected
