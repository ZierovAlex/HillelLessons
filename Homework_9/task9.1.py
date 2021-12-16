# Написать функцию которая принимает на вход параметры : список чисел любой
#    дины и число .
#    Функция должна проверить есть ли в списке 2 числа сума которых
#    еквивалентна числу переданому 2м параметром. Функция должна вернуть
#    булевое значение - результат поиска фукции.
#    Для проверки вызвать 2 раза функцию с разными тестовыми примерами.

import random


def operation(a, x):
    o = 1
    for i in range(0, len(a)):
        for j in range(o, len(a)):
#            print(a[i] + a[j])
            if a[i] + a[j] == x:
                return True
        o += 1
    return False


my_list = [random.randint(1, 10) for y in range(10)]
print(my_list)
my_integer = random.randint(2, 20)
print(my_integer)
print('')
print(operation(my_list, my_integer))
