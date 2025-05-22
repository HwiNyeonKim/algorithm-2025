def move_110(given_string):
    count = 0  # how many times the "110" appears

    stack = list()
    for char in given_string:
        stack.append(char)

        if (
            len(stack) > 2
            and stack[-1] == "0"
            and stack[-2] == "1"
            and stack[-3] == "1"
        ):
            for _ in range(3):
                stack.pop()

            count += 1

    inserting_string = "110" * count

    # 앞에서 "110"이 만들어지는 케이스를 전부 제거했으므로 (비슷한 아이디어: 올바른 괄호 문제)
    # dequeue에 남아있는 문자열들은 전부 "01" 로만 이루어지거나 마지막에 111이 붙은 경우이거나,
    # 전부 "10"으로만 이루어지거나 마지막에 "111"이 붙은 경우 뿐이다.

    temp_stack = list()
    while stack:
        if stack[-1] == "0":
            stack.append(inserting_string)
            while temp_stack:
                stack.append(temp_stack.pop())

            break
        else:
            temp_stack.append(stack.pop())

    if stack:
        return "".join(stack)

    return inserting_string + "".join(temp_stack)


def solution(s):
    return [move_110(string) for string in s]
