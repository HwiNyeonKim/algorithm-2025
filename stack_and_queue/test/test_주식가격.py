import pytest

from ..주식가격 import solution


@pytest.mark.parametrize(
    "prices, expected",
    [
        ([1, 2, 3, 2, 3], [4, 3, 1, 1, 0]),
        (
            [i for i in range(1, 100001)],
            [99999 - i for i in range(100000)],
        ),  # 테스트 케이스 1: 오름차순
        (
            [i for i in range(100000, 0, -1)],
            [1] * 99999 + [0],
        ),  # 테스트 케이스 2: 내림차순
        (
            [5000] * 100000,
            [99999 - i for i in range(100000)],
        ),  # 테스트 케이스 3: 동일한 값
        (
            [1] * 50000 + [100000] + [1] * 49999,
            # 테스트 케이스 4: 급상승 후 급하락
            [99999 - i for i in range(50000)]
            + [1]
            + [49998 - i for i in range(49999)],
        ),
    ],
)
def test_주식가격(prices, expected):
    answer = solution(prices)
    assert answer == expected
