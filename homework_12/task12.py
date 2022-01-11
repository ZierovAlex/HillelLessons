import random

m = input('Enter number of rows: Введите кол-во строк:')
while True:
    if m.isdigit():
        m = int(m)
        break
    else:
        m = input('You entered wrong! Please enter an integer!')
n = input('Enter the number of columns: Введите кол-во колонок:')
while True:
    if n.isdigit():
        n = int(n)
        break
    else:
        n = input('You entered wrong! Please enter an integer!')

my_matrix = [[random.randint(1, 50) for c in range(n)] for r in range(m)]
list_of_sums = []


def row_summarize(matrix, column, row):
    """Суммируем строки матрицы и добавляем каждый элемент суммы в
    соответствующую строку матрицы"""
    total = 0
    for r in range(row):
        for c in range(column):
            total += matrix[r][c]
        matrix[r].append(total)
        total = 0


def column_sumarize(list_of_sums, matrix, column, row):
    """Суммируем столбцы сатрицы и записываем в спомогательный одномерный
    список"""
    total = 0
    for r in range(column):
        for c in range(row):
            total += matrix[c][r]
        list_of_sums.append(total)
        total = 0


def my_print(matrix, m, n):
    for r in range(m):
        for c in range(n):
            print(matrix[r][c], end='\t')
        print('', end='  ')
        print(matrix[r][n])
    print()
    for c in list_of_sums:
        print(c, end='\t')


if __name__ == "__main__":
    row_summarize(my_matrix, n, m)
    column_sumarize(list_of_sums, my_matrix, n, m)
    my_print(my_matrix, m, n)
