# написать анонимную функцию которая приниммает 2 значения x,y  где y по
# умолчанию == числу . Результат работы функции - число x  в степени y.
# Используя функцию map  получить список чисел которые были созданы  в
# результате применения лямбда функции к каждому элементы. Для проверки
# привести тестовый пример в консоль.

import random

my_list = [random.randint(1, 20) for i in range(10)]
print(my_list)
my_func = list(map(lambda x, y=2: x ** y, my_list))
print(my_func)