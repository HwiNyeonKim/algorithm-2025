import pytest

from ..디스크_컨트롤러 import solution


@pytest.mark.parametrize(
    "jobs, expected",
    [
        [[[0, 3], [1, 9], [2, 6]], 9],
        [[[0, 9], [0, 4], [0, 5], [0, 7], [0, 3]], 13],
        [[[1, 9], [1, 4], [1, 5], [1, 7], [1, 3]], 13],
        [[[0, 5], [1, 2], [5, 5]], 6],
        [[[0, 3], [1, 9], [500, 6]], 6],
        [[[0, 4], [0, 3], [0, 2], [0, 1]], 5],
        [[[0, 20], [3, 4], [3, 5], [17, 2]], 19],
        [[[0, 5], [1, 5], [2, 4], [6, 1]], 7],
    ],
)
def test_disk_controller(jobs, expected):
    answer = solution(jobs)
    assert answer == expected
