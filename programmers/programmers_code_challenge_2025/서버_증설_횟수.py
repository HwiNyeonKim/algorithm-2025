import math


def solution(players, m, k):
    total_scale_out_count = 0
    # 0시-1시 부터 23시-24시까지 동작중인 서버의 수. 기본적으로 1개는 항상 동작중이다.
    servers = [1 for _ in range(24)]

    for time, player in enumerate(players):
        user_capacity = servers[time] * m - 1
        required_servers = max(math.ceil((player - user_capacity) / m), 0)

        for i in range(time, min(time + k, 24)):
            servers[i] += required_servers

        total_scale_out_count += required_servers

    return total_scale_out_count
