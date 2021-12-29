# import random
#
# # c - column
# # r - row
#
# # 1 size
# # m = int(input())
# m = 5
#
# # 2 generate matrix
# # my_matrix = [[random.randint(1, 50) for c in range(m)] for r in range(m)]
# my_matrix = [
#     [12, 90, 91, 43, 68],
#     [95, 19, 57, 20, 58],
#     [79, 94, 72, 44, 96],
#     [87, 27, 31, 13, 45],
#     [10, 61, 95, 30, 60]
# ]
#
# # summirize columns
# col_sum = [sum([my_matrix[r][c] for r in range(m)]) for c in range(m)]
#
#
# def my_sort(my_matrix, col_sum, m):
#     for j in range(m - 1):
#         for c in range(m - 1 - j):
#             if col_sum[c] > col_sum[c + 1]:
#                 # change list elements of col_sum
#                 col_sum[c], col_sum[c + 1] = col_sum[c + 1], col_sum[c]
#                 # change matrix columns
#                 for r in range(m):
#                     my_matrix[r][c], my_matrix[r][c + 1] = my_matrix[r][c + 1], \
#                                                    my_matrix[r][c]
#
#     for c in range(m):
#         if c % 2 == 0:
#             for j in range(m - 1):
#                 for r in range(m - 1 - j):
#                     if my_matrix[r][c] < my_matrix[r + 1][c]:
#                         my_matrix[r][c], my_matrix[r + 1][c] = my_matrix[r + 1][c], \
#                                                          my_matrix[r][c]
#         else:
#             for j in range(m - 1):
#                 for r in range(m - 1 - j):
#                     if my_matrix[r][c] > my_matrix[r + 1][c]:
#                         my_matrix[r][c], my_matrix[r + 1][c] = my_matrix[r + 1][c], \
#                                                          my_matrix[r][c]
#     return my_matrix, col_sum
#
# my_matrix, col_sum = my_sort(my_matrix, col_sum, m)
# for smth in my_matrix:
#     print(smth)
# print(col_sum)

import random

# c - column
# r - row

# 1 size
m = input('Пожалуйста введите целое число!')
while True:
    if m.isdigit():
        m = int(m)
        break
    else:
        m = input('Вы ввели неверно! Пожалуйста введите целое число!')

# 2 generate matrix
my_matrix = [[random.randint(1, 50) for c in range(m)] for r in range(m)]
for r in range(len(my_matrix)):
    for c in range(len(my_matrix)):
        print(my_matrix[r][c], end='\t')
    print()

# summarize columns
col_sum = [sum([my_matrix[r][c] for r in range(m)]) for c in range(m)]
for i in range(len(col_sum)):
    print(col_sum[i], end='\t')
print()
print()


def my_sort(matrix, summa, n):
    for j in range(n - 1):
        for c in range(n - 1 - j):
            if summa[c] > summa[c + 1]:
                # change list elements of col_sum
                summa[c], summa[c + 1] = summa[c + 1], summa[c]
                # change matrix columns
                for r in range(n):
                    matrix[r][c], matrix[r][c + 1] = matrix[r][c +
                                                               1], \
                                                     matrix[r][c]

    for c in range(n):
        for j in range(n - 1):
            for r in range(n - 1 - j):
                if ((c % 2 == 0) and (matrix[r][c] < matrix[r + 1][c])) \
                        or ((c % 2 != 0) and (matrix[r][c] > matrix[r +
                                                                    1][c])
                            ):
                    matrix[r][c], matrix[r + 1][c] = matrix[r + 1][
                                                         c], matrix[
                                                         r][c]
    return matrix, summa


def my_print(my_matrix1, col_sum1, m1):
    for r in range(m1):
        for c in range(m1):
            print(my_matrix1[r][c], end='\t')
        print()
    for c in range(m1):
        print(col_sum1[c], end='\t')


my_matrix, col_sum = my_sort(my_matrix, col_sum, m)
my_print(my_matrix, col_sum, m)
