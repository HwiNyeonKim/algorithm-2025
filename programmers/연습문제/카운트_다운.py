def solution(target):
    """
    - 1부터 20까지의 점수판.
    - single / double / triple 점수 존재
    - Bull에 맞으면 50점

    Args:
        target(int): 목표 점수

    Returns:
        List[int]: '최소 던진 횟수, Bull과 single을 던진 횟수'
    """
    singles = [50] + [i for i in range(1, 21)]
    doubles = [i * 2 for i in range(1, 21)]
    triples = [i * 3 for i in range(1, 21)]

    scores = [(score, 1) for score in singles] + [
        (score, 0) for score in doubles + triples
    ]  # (score, count of single & bull)

    dp = [[float("inf"), 0] for _ in range(target + 1)]  # score: [#, singles]
    dp[0] = [0, 0]  # to get score 0: 0 trials, 0 times of singles

    for i in range(target + 1):  # target score
        for score, single in scores:
            if i + score <= target:
                trial = dp[i][0] + 1
                single_count = dp[i][1] + single

                if trial < dp[i + score][0]:  # 더 적은 횟수로 도달이 가능한지?
                    dp[i + score] = [trial, single_count]
                elif (  # 같은 횟수지만 single & bull을 더 사용해서 도달이 가능한지?
                    trial == dp[i + score][0]
                    and single_count > dp[i + score][1]
                ):
                    dp[i + score] = [trial, single_count]

    return dp[target]
