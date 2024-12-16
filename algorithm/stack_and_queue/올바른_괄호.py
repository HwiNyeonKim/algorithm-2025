"""
Given:
    def solution(s):
        answer = True
        return True
"""


def solution(s):
    stack = list(")")

    for character in s:
        if character == "(":
            stack.append(character)
        else:
            opening_parenthesis = stack.pop()
            if opening_parenthesis != "(":
                return False

    return len(stack) == 1
