import pytest

from ..다단계_칫솔_판매 import solution


@pytest.mark.parametrize(
    "enroll, referral, seller, amount, expected",
    [
        [
            [
                "john",
                "mary",
                "edward",
                "sam",
                "emily",
                "jaimie",
                "tod",
                "young",
            ],
            ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
            ["young", "john", "tod", "emily", "mary"],
            [12, 4, 2, 5, 10],
            [360, 958, 108, 0, 450, 18, 180, 1080],
        ],
        [
            [
                "john",
                "mary",
                "edward",
                "sam",
                "emily",
                "jaimie",
                "tod",
                "young",
            ],
            ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
            ["sam", "emily", "jaimie", "edward"],
            [2, 3, 5, 4],
            [0, 110, 378, 180, 270, 450, 0, 0],
        ],
    ],
)
def test_다단계_칫솔_판매(enroll, referral, seller, amount, expected):
    answer = solution(enroll, referral, seller, amount)

    from devtools import debug

    debug(enroll, answer, expected)

    assert answer == expected
