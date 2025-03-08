from ..두_원_사이의_정수_쌍 import solution


def test_integer_pair_between_two_circles():
    answer = solution(r1=2, r2=3)
    assert answer == 20
