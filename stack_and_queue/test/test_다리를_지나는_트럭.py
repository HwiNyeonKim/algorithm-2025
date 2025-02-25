import pytest

from ..다리를_지나는_트럭 import solution


@pytest.mark.parametrize(
    "bridge_length, weight, truck_weights, expected",
    [
        [2, 10, [7, 4, 5, 6], 8],
        [100, 100, [10], 101],
        [100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10], 110],
    ],
)
def test_다리를_지나는_트럭(bridge_length, weight, truck_weights, expected):
    answer = solution(bridge_length, weight, truck_weights)
    assert answer == expected
