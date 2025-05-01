def solution(n, s):
    if n > s:
        return [-1]

    # a + b = const 일 때, ab는 |a - b|가 최소가 될 때 최대가 된다.
    # 즉, 이 문제에서는 길이 n인 배열의 원소들을 최대한 비슷한 값으로 설정해야 한다.

    # * 1. 기본값 설정: s를 n으로 나눈 몫만큼을 모든 원소가 기본값으로 가진다.
    # # # * 2. 최대값 찾기: 나머지를 최대한 균등하게 분배한다. 문제 조건에 따라 이 값은 뒤쪽부터 분배한다.
    base_value = s // n
    remainder = s % n

    return [base_value] * (n - remainder) + [base_value + 1] * remainder
