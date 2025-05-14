import math


def _get_coverage(n, station, w):
    start = 1 if station - w < 1 else station - w
    end = n if station + w >= n else station + w

    return start, end


def solution(n, stations, w):
    """
    Args:
        n (int): 아파트의 갯수
        stations (List[int]): 현재
        w (int): 전파의 도달 거리

    Returns:
        int: 모든 아파트에 전파를 전달하기 위해 증설해야 할 기지국의 갯수의 최솟값
    """
    already_covered = [_get_coverage(n, station, w) for station in stations]

    count = 0
    coverage = 2 * w + 1
    start = 1
    for covered_start, covered_end in already_covered:
        if covered_end > start:
            count += math.ceil((covered_start - start) / coverage)

        start = covered_end + 1

    if start <= n:
        count += math.ceil((n - start + 1) / coverage)

    return count
