def solution(targets):
    # 마지막 target이 동시타격 가능할 경우에도 카운팅이 되도록 dummy target 추가
    targets.append([10**8 + 1, 10**8 + 2])
    targets.sort(
        key=lambda target: target[0], reverse=True
    )  # (s, e) pair에 대해 s로 내름차순

    count = 0
    _, e = targets.pop()  # current_target
    while targets:
        ns, ne = targets.pop()  # next_target

        if e <= ns:
            # 동시 타격 불가능
            count += 1
            e = ne
        else:
            # 동시 타격 가능
            e = min(e, ne)

    return count
