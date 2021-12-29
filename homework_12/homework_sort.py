def my_sort(matrix, summa, n) -> object:
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


if __name__ == "__main__":
    import random
    m = input('Please enter an integer!')
    while True:
        if m.isdigit():
            m = int(m)
            break
        else:
            m = input('You entered wrong! Please enter an integer!')
    print()
    my_matrix = [[random.randint(1, 50) for c in range(m)] for r in range(m)]
    for r in range(len(my_matrix)):
        for c in range(len(my_matrix)):
            print(my_matrix[r][c], end='\t')
        print()
    col_sum = [sum([my_matrix[r][c] for r in range(m)]) for c in range(m)]
    for i in range(len(col_sum)):
        print(col_sum[i], end='\t')
    print()
    print()

    my_sort(my_matrix, col_sum, m)
    my_print(my_matrix, col_sum, m)
