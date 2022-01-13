__all__ = ["matrix_generation_with_summs", "matrix_2d_generator",
           "wired_matrix"]


def matrix_2d_generator():
    """Функция генерирует двумерный список заполненный случайными числами в
    диапазоне от 1 до 100"""
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

    my_matrix = [[random.randint(1, 100) for c in range(n)] for r in range(m)
                 ]
    return my_matrix


def matrix_generation_with_summs():
    """Домашнее задание 12. Печать матрицы размером N на M и выведение сумм
    столбцов и строк этой матрицы """
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

    row_summarize(my_matrix, n, m)
    column_sumarize(list_of_sums, my_matrix, n, m)
    my_print(my_matrix, m, n)


def wired_matrix():
    """Функция из домашней задачи 11 в которой печатается двумерный список
    М на М выводится сумма столбцов, матрица сортируется по возрастанию сумм
     столбцов и сортируются сами столбцы нечетные от меньшего к большему а
     четные наоборот"""
    import random

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

    my_sort(my_matrix, col_sum, m)
    my_print(my_matrix, col_sum, m)


if __name__ == "__main__":
    matrix_generation_with_summs()
    print()
    wired_matrix()
    a = matrix_2d_generator()
    print(a)
