import operator
from itertools import product

operations = [operator.add, operator.sub, operator.mul, operator.floordiv]


def solution(n, target_number):
    if n == target_number:
        return 1

    # n 을 i개 사용해서 만들 수 있는 경우의 수
    # - n을 i번 반복
    # - n을 (i - j)번 반복해서 만들 수 있는 경우의 수와 j번 반복해서 만들수 있는 경우의 수의 사칙연산
    dp = [set([int(str(n) * i)]) for i in range(1, 9)]
    dp.insert(0, set())

    for i in range(2, 9):
        for j in range(1, i):
            cartesian_product = product(dp[i - j], dp[j])

            for left, right in cartesian_product:
                for operation in operations:
                    try:
                        number = operation(left, right)
                    except ZeroDivisionError:
                        continue

                    dp[i].add(number)

        if target_number in dp[i]:
            return i

    return -1
