import pytest

from ..zigzag_conversion import convert


@pytest.mark.parametrize(
    "s, num_rows, expected",
    [
        ["PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"],
        ["PAYPALISHIRING", 4, "PINALSIGYAHRPI"],
    ]
)
def test_convert(s, num_rows, expected):
    answer = convert(s, num_rows)
    assert answer == expected
