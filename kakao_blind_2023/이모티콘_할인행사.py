from itertools import product


def solution(users, emoticons):
    results = list()  # (신규 구독자 수, 매출액)을 저장할 리스트

    discounts_product = product([10, 20, 30, 40], repeat=len(emoticons))
    for discounts in discounts_product:
        result = [0, 0]
        for user in users:
            minimum_discount_required, maximum_price = user
            price_paid = 0

            for i, discount in enumerate(discounts):
                if discount >= minimum_discount_required:
                    price_paid += emoticons[i] * (100 - discount) / 100

                if price_paid >= maximum_price:
                    result[0] += 1
                    price_paid = 0
                    break

            result[1] += price_paid
        results.append(result)

    results.sort(key=lambda x: (x[0], x[1]))
    return results[-1]
