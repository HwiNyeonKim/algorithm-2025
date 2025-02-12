import pytest

from programmers_code_challenge_2025 import solution_forklift_and_crane


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
    answer = solution_forklift_and_crane(storage, requests)
    assert answer == expected
