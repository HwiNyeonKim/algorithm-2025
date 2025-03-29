from functools import cmp_to_key


def solution(numbers):
    numbers = list(map(str, numbers))

    def _comporator(a: str, b: str):
        if a + b > b + a:
            return -1
        elif a + b < b + a:
            return 1
        else:
            return 0

    numbers.sort(key=cmp_to_key(_comporator))

    return str(int("".join(numbers)))
