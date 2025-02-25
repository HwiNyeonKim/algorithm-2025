from ..요격_시스템 import solution


def test_요격_시스템():
    targets = [[4, 5], [4, 8], [10, 14], [11, 13], [5, 12], [3, 7], [1, 4]]

    answer = solution(targets)
    expected_result = 3

    assert answer == expected_result
