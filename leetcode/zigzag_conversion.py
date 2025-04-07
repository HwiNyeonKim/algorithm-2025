from collections import deque


def convert(s: str, num_rows: int) -> str:
    # LeetCode 에서는 numRows로 되어있으나 Python에는 snake_case가 알맞아 보인다.

    # i-th column에 대하여...
    # 1. t % (num_rows - 1) == 0 인 경우
    #   - num_rows 만큼 column에 채우기
    # 2. t % (num_rows - 1) != 0 인 경우 (assume value = t % (num_rows - 1))
    #   - num_rows - value - 1번째 row에만 한 글자를 채운다
    if num_rows == 1:
        return s

    zigzag = list()  # 실제 구현에서는 편의상 column <-> rows를 반대로 만든다
    index = 0
    queue = deque(list(s))
    while queue:
        if index % (num_rows - 1) == 0:
            deque_count = min(num_rows, len(queue))
            row = [queue.popleft() for _ in range(deque_count)]

            # 결과 처리 편의성을 위해 마지막 row의 경우 빈 문자열을 채워 길이를 맞춰준다.
            row += [""] * (num_rows - deque_count)
        else:
            value = index % (num_rows - 1)
            char = queue.popleft()

            row = ["" for _ in range(num_rows)]
            row[num_rows - value - 1] = char

        zigzag.append(row)
        index += 1

    answer = list()
    for column in range(num_rows):
        for row in zigzag:
            answer.append(row[column])

    return "".join(answer)
