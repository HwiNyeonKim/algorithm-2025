from 연습문제 import solution_tower_of_hanoi


def test_tower_of_hanoi():
    answer = solution_tower_of_hanoi(2)
    assert answer == [[1, 2], [1, 3], [2, 3]]
