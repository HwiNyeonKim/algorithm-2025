from ..거스름돈 import solution


def test_change():
    answer = solution(n=5, money=[1, 2, 5])
    assert answer == 4
