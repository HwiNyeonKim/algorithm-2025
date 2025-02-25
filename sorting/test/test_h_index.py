from ..h_index import solution


def test_h_index():
    citations = [3, 0, 6, 1, 5]
    answer = solution(citations)

    assert answer == 3
