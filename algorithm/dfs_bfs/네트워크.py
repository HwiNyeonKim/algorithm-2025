from collections import deque


def solution_bfs(n, computers):
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


def solution_dfs(n, computers):
    # DFS
    network_count = 0
    visited = [False] * n
    while not all(visited):
        network_entry_point = visited.index(False)
        stack = [network_entry_point]

        network_count += 1
        while stack:
            computer = stack.pop()

            current_network = computers[computer]
            if visited[computer]:
                continue

            visited[computer] = True

            for next_computer, connected in enumerate(current_network):
                if connected:
                    stack.append(next_computer)

    return network_count
