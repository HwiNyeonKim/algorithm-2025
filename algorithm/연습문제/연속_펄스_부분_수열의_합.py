from collections import deque


def solution(sequence):
    ranges = list()  # element: index of (start, end)
    largest_partial_sum = max(sequence, key=abs)

    queue = deque(sequence)
    index = 0
    while queue:
        start_index = index
        end_index = index
        current_value = queue.popleft()

        while queue:
            index += 1
            next_value = queue.popleft()

            if current_value * next_value <= 0:
                end_index = index
                current_value = next_value
            else:
                # 동일 부호
                queue.appendleft(next_value)
                break

        ranges.append((start_index, end_index))

    for start, end in ranges:
        numbers = sequence[start : end + 1]
        pulse = [1, -1] * (len(numbers) // 2) + [1]

        partial_sum = sum([a * b for a, b in zip(numbers, pulse)])

        largest_partial_sum = max(
            partial_sum, -partial_sum, largest_partial_sum
        )

    return largest_partial_sum
