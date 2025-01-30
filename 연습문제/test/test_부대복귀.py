import pytest

from 연습문제 import solution_2


@pytest.mark.parametrize(
    "n, roads, sources, destination, expected",
    [
        (3, [[1, 2], [2, 3]], [2, 3], 1, [1, 2]),
        (
            5,
            [[1, 2], [1, 4], [2, 4], [2, 5], [4, 5]],
            [1, 3, 5],
            5,
            [2, -1, 0],
        ),
    ],
)
def test_부대복귀(n, roads, sources, destination, expected):
    answer = solution_2(n, roads, sources, destination)
    assert answer == expected
