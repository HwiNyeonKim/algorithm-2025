from collections import defaultdict


def solution(clothes):
    stock = defaultdict(list)
    for cloth in clothes:
        name, category = cloth
        stock[category].append(name)

    kinds = 1
    for cloth_list in stock.values():
        kinds *= len(cloth_list) + 1

    return kinds - 1
