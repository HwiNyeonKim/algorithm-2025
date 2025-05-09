def solution(matrix_sizes):
    sizes = [
        matrix_size[0] for matrix_size in matrix_sizes[1:]
    ]
    first = matrix_sizes[0][0]
    last = matrix_sizes[-1][1]
    # [[5, 3], [3, 10], [10, 6]] -> [5, 3, 10, 6]으로 serialize
    # 그런데, 첫 값과 마지막 값은 결국 최종 계산에 반드시 들어가야 하므로 따로 빼둔다.
    # 즉, 반복문 내에서 계산에 이용되는 serialized values는 [3, 10]

    # sizes에서 최댓값을 찾아, 그 최댓값을 가지는 행렬끼리 먼저 곱한다.

    count = 0
    while sizes:
        index = sizes.index(max(sizes))

        row = first if index == 0 else sizes[index - 1]
        middle = sizes[index]
        column = last if index == len(sizes) - 1 else sizes[index + 1]
        count += row * middle * column

        sizes.pop(index)

    return count
