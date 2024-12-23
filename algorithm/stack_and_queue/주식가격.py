def solution(prices):
    answer = [0] * len(prices)
    stack = list()  # 가격 하락이 발생하지 않은 주식 가격의 index만 저장

    for i in range(len(prices)):
        while stack:
            last_price = prices[stack[-1]]
            next_price = prices[i]

            if last_price > next_price:
                j = stack.pop()
                answer[j] = i - j
            else:
                break

        stack.append(i)

    while stack:
        index = stack.pop()
        answer[index] = len(prices) - index - 1

    return answer
