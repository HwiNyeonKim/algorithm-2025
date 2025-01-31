from kakao_blind_2020 import solution_lock_and_key


def test_solution_lock_and_key():
    answer = solution_lock_and_key(
        [[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    )
    assert answer is True
