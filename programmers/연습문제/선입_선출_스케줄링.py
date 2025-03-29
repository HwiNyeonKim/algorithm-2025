def calc_tasks_on_turn(turn, cores):
    return sum((turn // core) + 1 for core in cores)


def calc_minimum_turn_to_finish_tasks(n, cores):
    minimum_turn = 0
    maximum_turn = 10_000 * 50_000  # 작업 처리 시간 최대값 * 일의 개수 최대값

    while minimum_turn < maximum_turn:
        mid = (minimum_turn + maximum_turn) // 2
        handled_tasks = calc_tasks_on_turn(mid, cores)

        if handled_tasks < n:
            minimum_turn = mid + 1
        else:
            maximum_turn = mid

    return min(minimum_turn, maximum_turn)


def get_idle_cores(turn, cores):
    idle_cores = list()
    for index, core in enumerate(cores, start=1):
        if turn % core == 0:
            idle_cores.append(index)

    return idle_cores


def solution(n, cores):
    minimum_turn_to_finish = calc_minimum_turn_to_finish_tasks(n, cores)

    # 모든 작업을 처리하는데 필요한 시간 - 1일 때, 몇 개의 작업이 남았는지 확인한다.
    n -= calc_tasks_on_turn(minimum_turn_to_finish - 1, cores)

    # 마지막으로 할당될 작업들을 할당받을 수 있는 코어들을 확인한다.
    idle_cores = get_idle_cores(minimum_turn_to_finish, cores)

    return idle_cores[n - 1]
