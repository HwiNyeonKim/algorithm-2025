from math import ceil, floor, sqrt


def solution(r1, r2):
    # 1사분면 위의 두 원 사이의 점들을 전부 찾은 후 4배를 해 준다
    points = 0

    # y축 상의 점들까지 함께 고려한다.
    for y in range(1, r2 + 1):
        # x축 상의 점들은 y축 상의 결과와 동일하므로 계산은 스킵하고 마지막에 4배를 하는것으로 적용
        x_min = ceil(sqrt(r1**2 - y**2)) if y <= r1 else 0
        x_max = floor(sqrt(r2**2 - y**2))

        if x_min > x_max:
            break

        points += x_max - x_min + 1

    return 4 * points
