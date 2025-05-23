import pytest

from ..hash_divided_string import string_hash


@pytest.mark.parametrize(
    "s, k, expected",
    [
        ["abcd", 2, "bf"],
        ["mxz", 3, "i"],
    ],
)
def test_string_hash(s, k, expected):
    answer = string_hash(s, k)
    assert answer == expected
