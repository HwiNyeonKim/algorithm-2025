import pytest

from ..충돌_위험_찾기 import solution


@pytest.mark.parametrize(
    "points, routes, expected",
    [
        ([[3, 2], [6, 4], [4, 7], [1, 4]], [[4, 2], [1, 3], [2, 4]], 1),
        (
            [[3, 2], [6, 4], [4, 7], [1, 4]],
            [[4, 2], [1, 3], [4, 2], [4, 3]],
            9,
        ),
        (
            [[2, 2], [2, 3], [2, 7], [6, 6], [5, 2]],
            [[2, 3, 4, 5], [1, 3, 4, 5]],
            0,
        ),
    ],
)
def test_solution(points, routes, expected):
    assert solution(points, routes) == expected
