def solution(r1, r2):
    # 1. x축상의 점의 갯수(양의 방향만 계산): 마지막에 4배를 해 준다.
    points = r2 - r1 + 1  # 원 위의 점을 포함하므로

    # 2. 1사분면의 점의 갯수: 마찬가지로 최종적으로 4배를 해 준다.
    for x in range(1, r2 + 1):
        for y in range(1, r2 + 1):
            squared_distance = x**2 + y**2
            if r1**2 <= squared_distance <= r2**2:
                points += 1

    return points * 4
