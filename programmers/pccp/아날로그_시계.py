def to_seconds(h, m, s):
    return h * 3600 + m * 60 + s


def solution(h1, m1, s1, h2, m2, s2):
    current = to_seconds(h1, m1, s1)
    end = to_seconds(h2, m2, s2)

    count = 0

    while current < end:
        # 자정 및 정오에 대한 특수처리
        if current == 0 or current == 12 * 3600:
            count += 1
            current += 1
            continue

        hours = (current // 3600) % 12
        minutes = (current % 3600) // 60
        seconds = current % 60

        # 초침 sweep 범위 계산
        second_hand_from = seconds * 6
        second_hand_to = (seconds + 1) * 6

        # 분침 sweep 범위 계산
        minutes_hand_from = minutes * 6 + seconds * 0.1
        minutes_hand_to = minutes * 6 + (seconds + 1) * 0.1

        # 초침과 분침이 겹치는 경우 카운트
        # 단, 초침의 이동이 종료될 때 겹치는 경우는 카운트하지 않고,
        # 초침의 이동이 시작될 때 겹치는 경우만 카운트한다.
        if (
            second_hand_from <= minutes_hand_from
            and minutes_hand_to < second_hand_to
        ):
            count += 1

        # 시침 sweep 범위 계산
        hours_hand_from = hours * 30 + minutes * 0.5 + seconds * (1 / 120)
        hours_hand_to = hours * 30 + minutes * 0.5 + (seconds + 1) * (1 / 120)

        # 초침과 시침이 겹치는 경우 카운트
        if (
            second_hand_from <= hours_hand_from
            and hours_hand_to < second_hand_to
        ):
            count += 1

        current += 1

    # 초침의 이동이 종료되는 시점에 겹치는 경우는 카운트하지 않았으므로,
    # 마지막에 초침과 분침이 12를 가리키며 겹치는 경우를 특수처리로 카운트한다.
    if m2 == 0 and s2 == 0:
        count += 1

    return count
