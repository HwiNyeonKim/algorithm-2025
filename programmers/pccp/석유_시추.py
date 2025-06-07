from collections import deque


def solution(land):
    n = len(land)
    m = len(land[0])

    oils = [0] * m  # 각 열별 시추 가능한 석유량
    visited = set()  # 전체 방문 좌표 저장

    # 모든 좌표를 순회하면서 석유 덩어리 찾기
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and (i, j) not in visited:
                # 현재 석유 덩어리에 포함된 모든 좌표
                current_oil = set()
                queue = deque([(i, j)])

                while queue:
                    x, y = queue.popleft()

                    if (x, y) in visited:
                        continue

                    visited.add((x, y))
                    current_oil.add((x, y))

                    for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                        nx = x + dx
                        ny = y + dy

                        if 0 <= nx < n and 0 <= ny < m and land[nx][ny] == 1:
                            queue.append((nx, ny))

                # 현재 석유 덩어리가 있는 모든 열에 석유량 추가
                oil_size = len(current_oil)
                columns = set(y for _, y in current_oil)
                for col in columns:
                    oils[col] += oil_size

    return max(oils)
