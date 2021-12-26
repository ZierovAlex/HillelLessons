 # создать функцию генератор ПРОСТЫХ чисел в дипазоне заданых 2мя аргументами
# чисел. Вывести в консоль результат работы функции-генератора  в диапазоне
# 1,100 в одну строчку через пробел

# def prime_numbers_generator(x):
#     if x == 1:
#         return False
#     else:
#         for i in range(2, x):
#             if x % i == 0:
#                 return False
#         return True
#
#
# prime = ([x for x in range(1, 100) if prime_numbers_generator(x)])
# print(*prime)
#
# from sympy import isprime
#
#
# def prime_numbers(n):
#     for prime in range(n):
#         if isprime(i):
#             yield i
#
#
# a = prime_numbers(100)
#
# for i in a:
#     print(i, end=" ")


def prime_numbers(n):
    o = 2
    for i in range(2, n):
        for j in range(2, o):
            if i % j == 0:
                break
        else:
            yield i
        o += 1


a = prime_numbers(101)

for i in a:
    print(i, end=" ")
