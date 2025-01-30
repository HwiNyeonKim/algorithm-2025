from collections import deque


def solution(bridge_length, weight, truck_weights):
    # 1. Initial State
    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    current_weight = 0
    time = 0

    while bridge:
        # 2. 다리 위 트럭들 전부 한 칸씩 진행
        time += 1
        outgoing_truck = bridge.popleft()
        current_weight -= outgoing_truck

        if truck_weights:
            incoming_truck = truck_weights[0]

            # 3. 새 트럭 진입 불가
            if current_weight + incoming_truck > weight:
                bridge.append(0)
                continue

            # 4. 새 트럭 진입 가능
            bridge.append(incoming_truck)
            truck_weights.popleft()
            current_weight += incoming_truck

    return time
