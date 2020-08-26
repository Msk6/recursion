numbers = [
    [1, 2, 3, 4],
    [3, 6, [5, 6], 8, 2,[2, 4], 9],
    [4, 2, [6, 7, [2, 6, 1]]]
]



def sum_inside(arr):
    total = 0
    for i in arr:
        if type(i) != list:
            total = total + i

        else:
            total = total + sum_inside(i)

    return total

print(f'----- The sum is: {sum_inside(numbers)} -----')