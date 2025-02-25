from ..자물쇠와_열쇠 import solution


def test_solution_lock_and_key():
    answer = solution(
        [[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    )
    assert answer is True
