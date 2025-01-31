def solution(n):
    answer = list()

    def hanoi(disk_to_move, from_, via, to):
        if disk_to_move == 1:
            answer.append([from_, to])
        else:
            hanoi(disk_to_move - 1, from_=from_, via=to, to=via)
            answer.append([from_, to])
            hanoi(disk_to_move - 1, from_=via, via=from_, to=to)

    hanoi(n, 1, 2, 3)

    return answer
