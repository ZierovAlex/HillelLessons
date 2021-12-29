import random
import homework_sort

# c - column
# r - row

# 1 size
m = input('Please enter an integer!')
while True:
    if m.isdigit():
        m = int(m)
        break
    else:
        m = input('You entered wrong! Please enter an integer!')

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

homework_sort.my_sort(my_matrix, col_sum, m)
homework_sort.my_print(my_matrix, col_sum, m)
