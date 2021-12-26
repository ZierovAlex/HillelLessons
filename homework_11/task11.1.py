import random

# c - column
# r - row

# 1 size
# m = int(input())
m = 5

# 2 generate matrix
# my_matrix = [[random.randint(1, 50) for c in range(m)] for r in range(m)]
my_matrix = [
    [12, 90, 91, 43, 68],
    [95, 19, 57, 20, 58],
    [79, 94, 72, 44, 96],
    [87, 27, 31, 13, 45],
    [10, 61, 95, 30, 60]
]

# summirize columns
col_sum = [sum([my_matrix[r][c] for r in range(m)]) for c in range(m)]


def my_sort(my_matrix, col_sum, m):
    for j in range(m - 1):
        for c in range(m - 1 - j):
            if col_sum[c] > col_sum[c + 1]:
                # change list elements of col_sum
                col_sum[c], col_sum[c + 1] = col_sum[c + 1], col_sum[c]
                # change matrix columns
                for r in range(m):
                    my_matrix[r][c], my_matrix[r][c + 1] = my_matrix[r][c + 1], \
                                                   my_matrix[r][c]

    for c in range(m):
        if c % 2 == 0:
            for j in range(m - 1):
                for r in range(m - 1 - j):
                    if my_matrix[r][c] > my_matrix[r + 1][c]:
                        my_matrix[r][c], my_matrix[r + 1][c] = my_matrix[r + 1][c], \
                                                         my_matrix[r][c]
        else:
            for j in range(m - 1):
                for r in range(m - 1 - j):
                    if my_matrix[r][c] < my_matrix[r + 1][c]:
                        my_matrix[r][c], my_matrix[r + 1][c] = my_matrix[r + 1][c], \
                                                         my_matrix[r][c]
    return my_matrix, col_sum

my_matrix, col_sum = my_sort(my_matrix, col_sum, m)
for smth in my_matrix:
    print(smth)
print(col_sum)
