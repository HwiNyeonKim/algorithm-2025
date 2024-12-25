def _is_valid(queens, row, col):
    # 1. 가로: 확인할 필요 없음
    # 2. 세로: 같은 Column이 있는지 확인
    # 3. 대각선: row의 차이만큼 column의 차이가 있는지 확인
    for row_placed, col_placed in queens:
        if col == col_placed or abs(row - row_placed) == abs(col - col_placed):
            return False

    return True


def solution(n):
    count = 0
    queens = list()  # (row, col)

    def backtracking(row):
        nonlocal count

        if row == n:
            # all queens are placed
            count += 1
            return

        for col in range(n):
            if _is_valid(queens, row, col):
                queens.append((row, col))
                backtracking(row + 1)
                queens.pop()

    backtracking(0)

    return count
