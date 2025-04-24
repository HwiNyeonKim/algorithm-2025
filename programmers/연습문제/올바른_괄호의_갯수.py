from itertools import permutations


def is_correct(candidate):
    """Check given parenthesis candidate is correct or not

    Args:
        candidate (List[str]): 올바른지 판별하려는 괄호쌍 후보
    Returns:
        Bool: 올바른 괄호쌍이면 True, 아니면 False
    """
    stack = list()
    for char in candidate:
        if char == '(':
            stack.append(char)
        else:
            try:
                stack.pop()
            except IndexError:
                return False

    return len(stack) == 0


def solution(n):
    """

    Args:
        n (int): 괄호쌍의 갯수
    Returns:
        int: 만들 수 있는 올바른 괄호 쌍의 갯수
    """
    # 1. Backtracking
    # 2. 2**14 = 약 16,000개로 Brute Force로도 풀이가 가능할 듯.

    # * 일단 먼저 BruteForce로 풀어본다.
    remaining = ['('] * n + [')'] * n
    candidates = set()
    for candidate in permutations(remaining, r=2 * n):
        candidates.add(candidate)

    count = 0
    for candidate in candidates:
        if is_correct(candidate):
            count += 1

    return count
