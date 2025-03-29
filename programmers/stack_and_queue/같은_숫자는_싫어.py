# from collections import deque

"""
Default Given:
    def solution(arr):
        answer = []
        return answer
"""


def solution(arr):
    # stack = deque()
    stack = list()
    stack.append(arr[0])

    for element in arr:
        peeked = stack[-1]

        if peeked != element:
            stack.append(element)

    # return list(stack)
    return stack
