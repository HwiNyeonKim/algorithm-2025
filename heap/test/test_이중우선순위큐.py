import pytest

from heap import solution_double_priority_queue


@pytest.mark.parametrize(
    "operations, expected",
    [
        [["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"], [0, 0]],
        [
            [
                "I -45",
                "I 653",
                "D 1",
                "I -642",
                "I 45",
                "I 97",
                "D 1",
                "D -1",
                "I 333",
            ],
            [333, -45],
        ],
        [["I 2", "I 2", "I 3", "I 3", "D 1", "D -1"], [3, 2]],
        [["I 0", "I -1", "I -5", "I 10", "D 1", "D -1"], [0, -1]],
        [["I 5", "I 3", "I 7", "D -1", "D 1"], [5, 5]],
        [["I 4", "I 2", "D 1", "D 1", "D -1"], [0, 0]],
    ],
)
def test_double_priority_queue(operations, expected):
    answer = solution_double_priority_queue(operations)
    assert answer == expected
