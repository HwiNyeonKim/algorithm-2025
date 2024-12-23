def solution(prices):
    # Trial #1 : Failed (Timed out)
    index = 1
    answer = [0]

    while index < len(prices):
        current_price = prices[-index - 1]
        next_prices = prices[-index:]

        seconds = 0
        for next_price in next_prices:
            seconds += 1

            if current_price > next_price:
                break

        answer.append(seconds)
        index += 1

    return answer[::-1]
