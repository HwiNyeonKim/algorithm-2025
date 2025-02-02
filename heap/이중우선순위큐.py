def solution(operations):
    values = list()

    count = 0
    is_sorted = False

    while count < len(operations):
        operation, value = operations[count].split()
        count += 1

        if operation == "I":
            values.append(int(value))
            is_sorted = False
            continue

        # 여기에 도달했다면 Operation은 D이다.
        if not values:
            continue

        if not is_sorted:
            values.sort()
            is_sorted = True

        if value == "1":
            values.pop()
        else:
            values.pop(0)

    values.sort()

    return [values[-1], values[0]] if values else [0, 0]
