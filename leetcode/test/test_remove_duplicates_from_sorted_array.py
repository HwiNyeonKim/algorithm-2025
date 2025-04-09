import pytest

from ..remove_duplicates_from_sorted_array import remove_duplicates


@pytest.mark.parametrize(
    "nums, expected",
    [
        [[1, 1, 2], 2],
        [[0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5],
    ],
)
def test_remove_duplicates(nums, expected):
    answer = remove_duplicates(nums)
    assert answer == expected
