import pytest

from ..영어_끝말잇기 import solution


@pytest.mark.parametrize(
    "n, words, expected",
    [
        [
            3,
            [
                "tank",
                "kick",
                "know",
                "wheel",
                "land",
                "dream",
                "mother",
                "robot",
                "tank",
            ],
            [3, 3],
        ],
        [
            5,
            [
                "hello",
                "observe",
                "effect",
                "take",
                "either",
                "recognize",
                "encourage",
                "ensure",
                "establish",
                "hang",
                "gather",
                "refer",
                "reference",
                "estimate",
                "executive",
            ],
            [0, 0],
        ],
        [2, ["hello", "one", "even", "never", "now", "world", "draw"], [1, 3]],
    ],
)
def test_english_word_chain(n, words, expected):
    assert solution(n, words) == expected
