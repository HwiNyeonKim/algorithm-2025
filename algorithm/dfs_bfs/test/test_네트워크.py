import pytest
from dfs_bfs import solution_1


@pytest.mark.parametrize(
    "n, computers, expected",
    [
        # [3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]], 2],
        [3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]], 1],
    ],
)
def test_네트워크(n, computers, expected):
    answer = solution_1(n, computers)

    assert answer == expected
