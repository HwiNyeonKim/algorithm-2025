import pytest
from hash import solution_1


@pytest.mark.parametrize(
    "phone_book, expected",
    [
        [["119", "97674223", "1195524421"], False],
        [["123", "456", "789"], True],
        [["12", "123", "1235", "567", "88"], False],
    ],
)
def test_전화번호_목록(phone_book, expected):
    answer = solution_1(phone_book)
    assert answer == expected
