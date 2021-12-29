import random
#
# my_list = [[random.randint(10, 99) for i in range(5)] for j in range(5)]
# my_list1 = []
#
# print(my_list)
#
#
# counter = 0
# summ = 0
# while counter < len(my_list):
#
#     for u in range(len(my_list)-1):
#         print(my_list[u][counter],end=' ')
#         summ += my_list[u][counter]
#
#     my_list1.append(summ)
#     counter += 1
#     summ = 0
#
# print(my_list1)
# my_list.append(my_list1)
# print(my_list)
#
# for o in my_list:
#     print(o)


# Сортировка пузырьком обычного случайно генерируемого списка
# N = 10
# a = [random.randint(10,99) for i in range(N)]
# print(a)
#
# for i in range(N - 1):
#     for j in range(N - i - 1):
#         if a[j] > a[j + 1]:
#
#             a[j], a[j + 1] = a[j + 1], a[j]
#     print(a)
#
# print(a)


# a = [[random.randint(10, 99) for i in range(5)] for j in range(5)]
# N = len(a)
# for illustrate in range(N):
#     print(a[illustrate])
# print()
# for i in range(N - 1):
#     for j in range(N - i - 1):
#         if a[j][i] > a[j + 1][i]:
#
#             a[j][i], a[j + 1][i] = a[j + 1][i], a[j][i]
#     print(a)
#
# for illustrate1 in range(N):
#     print(a[illustrate1])

# a = [
#     [12, 90, 91, 43, 68],
#     [95, 19, 57, 20, 58],
#     [79, 94, 72, 44, 96],
#     [87, 27, 31, 13, 45],
#     [10, 61, 95, 30, 60]
# ]
# N = len(a)
# for illustrate in range(N):
#     print(a[illustrate])
# print()
# for i in range(N):
#     for j in range(N):
#         print(a[j][i],end="    ")
#     print()

a = [
    [12, 90, 91, 43, 68],
    [95, 19, 57, 20, 58],
    [79, 94, 72, 44, 96],
    [87, 27, 31, 13, 45],
    [10, 61, 95, 30, 60]
]
N = len(a)
for illustrate in range(N):
    print(a[illustrate])
print()
for y in range(N):
    for i in range(N - 1):
        for j in range(N):
            if a[i][j] > a[i + 1][j]:
                a[i][j], a[i+1][j] = a[i+1][j], a[i][j]

for vac in a:
    print(vac)











def my_sort(my_matrix, col_sum, m):
    for j in range(m - 1):
        # flag = True
        for i in range(m - 1 - j):
            if col_sum[i] > col_sum[i + 1]:
                col_sum[i], col_sum[i + 1] = col_sum[i + 1], col_sum[i]
                # flag = False
        # if flag:
            # break
    return col_sum

