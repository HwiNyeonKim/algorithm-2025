import pytest

from programmers_code_challenge_2025 import solution_odd_even_tree


@pytest.mark.parametrize(
    "nodes, edges, expected",
    [
        [[11, 9, 3, 2, 4, 6], [[9, 11], [2, 3], [6, 3], [3, 4]], [1, 0]],
        [
            [9, 15, 14, 7, 6, 1, 2, 4, 5, 11, 8, 10],
            [
                [5, 14],
                [1, 4],
                [9, 11],
                [2, 15],
                [2, 5],
                [9, 7],
                [8, 1],
                [6, 4],
            ],
            [2, 1],
        ],
    ],
)
def test_odd_even_tree(nodes, edges, expected):
    answer = solution_odd_even_tree(nodes, edges)
    assert answer == expected
