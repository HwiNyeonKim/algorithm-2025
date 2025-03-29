from collections import defaultdict


def is_accessible(storage, location, visited):
    n = len(storage)
    m = len(storage[0])
    row, col = location
    # 테두리인지?
    if row == 0 or col == 0 or row == n - 1 or col == m - 1:
        return True

    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dir_ in dirs:
        d_row, d_col = dir_
        next_row, next_col = row + d_row, col + d_col
        if (
            storage[next_row][next_col] == " "
            and (next_row, next_col) not in visited
        ):
            visited.add((next_row, next_col))
            if is_accessible(storage, (next_row, next_col), visited):
                return True

    return False


def pop_with_forklift(storage, containers, name):
    locations = containers[name]
    removable = list()
    remaining = list()

    for location in locations:
        visited = set()
        if is_accessible(storage, location, visited):
            removable.append(location)
        else:
            remaining.append(location)

    for r, c in removable:
        storage[r][c] = " "
    containers[name] = remaining


def pop_with_crane(storage, containers, name):
    locations = containers[name]
    for row, col in locations:
        storage[row][col] = " "
    containers[name] = list()


def solution(storage, requests):
    for i, row in enumerate(storage):
        storage[i] = list(row)

    # 화물 이름과 위치를 hash table로 기록하기
    containers = defaultdict(list)  # key: value = container name : locations
    for row, names in enumerate(storage):
        for col, name in enumerate(names):
            containers[name].append((row, col))

    for request in requests:
        if len(request) == 1:
            pop_with_forklift(storage, containers, request)
        elif len(request) == 2:
            pop_with_crane(storage, containers, request[0])
        else:
            raise Exception("Wrong Request")

    answer = 0
    for locations in containers.values():
        answer += len(locations)

    return answer
