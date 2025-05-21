from collections import defaultdict


def solution(a):
    if len(a) < 2:
        return 0

    counter = defaultdict(int)

    for number in a:
        counter[number] += 1

    answer = 0
    for key, count in counter.items():
        if 2 * count <= answer:
            # 계산 해 봤자, 의미가 없다. 이미 계산된 것들 중에 더 좋은 답이 있다.
            continue

        used = [False] * len(a)
        start_sequence_length = 0

        for i in range(len(a) - 1):
            if not used[i] and not used[i + 1]:
                if a[i] != a[i + 1] and (a[i] == key or a[i + 1] == key):
                    start_sequence_length += 2
                    used[i] = True
                    used[i + 1] = True

        answer = max(answer, start_sequence_length)

    return answer
