import math


def get_idle_cores(turn, cores):
    idle_cores = list()
    for index, core in enumerate(cores, start=1):
        if turn % core == 0:
            idle_cores.append(index)

    return idle_cores


def solution(n, cores):
    turn = 0

    cycle_turns = math.lcm(*cores)
    tasks_per_cycle = sum(cycle_turns // core for core in cores)
    while n > tasks_per_cycle:
        n -= tasks_per_cycle

    while n > 0:
        idle_cores = get_idle_cores(turn, cores)

        n -= len(idle_cores)

        turn += 1

    return idle_cores[n + len(idle_cores) - 1]
