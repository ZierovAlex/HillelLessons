# создать функцию генератор ПРОСТЫХ чисел в дипазоне заданых 2мя аргументами
# чисел. Вывести в консоль результат работы функции-генератора  в диапазоне
# 1,100 в одну строчку через пробел

def prime_numbers_generator(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


prime = ([x for x in range(1, 100) if prime_numbers_generator(x)])
print(*prime)
