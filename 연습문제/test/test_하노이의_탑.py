from ..하노이의_탑 import solution


def test_tower_of_hanoi():
    answer = solution(2)
    assert answer == [[1, 2], [1, 3], [2, 3]]
