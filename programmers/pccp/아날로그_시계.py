def to_seconds(h, m, s):
    return h * 3600 + m * 60 + s


def solution(h1, m1, s1, h2, m2, s2):
    current = to_seconds(h1, m1, s1)
    end = to_seconds(h2, m2, s2)

    count = 0

    while current < end:
        # 초침, 분침, 시침이 모두 겹치는 경우에 대한 특수처리
        if current == 0 or current == 12 * 3600:
            count += 1
            current += 1
            continue

        hours = (current // 3600) % 12
        minutes = (current % 3600) // 60
        seconds = current % 60

        second_hand_from = seconds * 6
        second_hand_to = (seconds + 1) * 6

        minutes_hand_from = minutes * 6 + seconds * 0.1
        minutes_hand_to = minutes * 6 + (seconds + 1) * 0.1

        if (
            second_hand_from <= minutes_hand_from
            and minutes_hand_to <= second_hand_to
        ):
            count += 1 if minutes_hand_to != 360 else 0

        hours_hand_from = hours * 30 + minutes * 0.5 + seconds * (1 / 120)
        hours_hand_to = hours * 30 + minutes * 0.5 + (seconds + 1) * (1 / 120)

        if (
            second_hand_from <= hours_hand_from
            and hours_hand_to <= second_hand_to
        ):
            # 12시가 되는 순간이 end에 포함된 경우에만 360도에 도달하는 순간을 카운트
            if hours_hand_to == 360 and end == 12 * 3600:
                count += 1
            else:
                count += 1 if hours_hand_to != 360 else 0

        current += 1

    if h2 != 12 and m2 == 0 and s2 == 0:
        count += 1

    return count
