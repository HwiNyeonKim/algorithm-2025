def kandane(sequence, starting_pulse):
    current_max = sequence[0] * starting_pulse
    global_max = sequence[0] * starting_pulse

    for index, value in enumerate(sequence[1:], start=1):
        pulse = starting_pulse if index % 2 == 0 else -starting_pulse
        partial_sum = value * pulse
        current_max = max(partial_sum, current_max + partial_sum)
        global_max = max(global_max, current_max)

    return global_max


def solution(sequence):
    return max(kandane(sequence, 1), kandane(sequence, -1))
