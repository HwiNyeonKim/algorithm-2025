from collections import deque


def solution(n, computers):
    # 1. BFS
    network_count = 0
    visited = [False] * n
    while not all(visited):
        network_entry_point = visited.index(False)
        queue = deque([network_entry_point])

        network_count += 1
        while queue:
            computer = queue.popleft()

            current_network = computers[computer]
            if visited[computer]:
                continue

            visited[computer] = True

            for next_computer, connected in enumerate(current_network):
                if connected:
                    queue.append(next_computer)

    return network_count
