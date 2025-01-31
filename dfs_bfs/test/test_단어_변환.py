import pytest

from dfs_bfs import solution_word_transform


@pytest.mark.parametrize(
    "begin, target, words, expected",
    [
        ("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"], 4),
        ("hit", "cog", ["hot", "dot", "dog", "lot", "log"], 0),
    ],
)
def test_word_transform(begin, target, words, expected):
    answer = solution_word_transform(begin, target, words)
    assert answer == expected
