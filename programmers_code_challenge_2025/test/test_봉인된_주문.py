import pytest

from programmers_code_challenge_2025 import solution_sealed_spell


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
    answer = solution_sealed_spell(n, bans)
    assert answer == expected
