import pytest

from ..지게차와_크레인 import solution


@pytest.mark.parametrize(
    "storage, requests, expected",
    [
        [["AZWQY", "CAABX", "BBDDA", "ACACA"], ["A", "BB", "A"], 11],
        [
            ["HAH", "HBH", "HHH", "HAH", "HBH"],
            ["C", "B", "B", "B", "B", "H"],
            4,
        ],
    ],
)
def test_forklift_and_crane(storage, requests, expected):
    answer = solution(storage, requests)
    assert answer == expected
