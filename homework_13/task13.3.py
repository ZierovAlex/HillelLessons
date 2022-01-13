import random
# Подключаем модуль с помощью import *, реализована опция __all__
from task13_1 import *

# Проверяем что работает каждый вид сортировки из подключенного модуля

my_list = [random.randint(1,100) for i in range(20)]
print(my_list)
quick_sort(my_list)
print(my_list, "\n")
my_list1 = [random.randint(1, 100) for j in range(20)]
print(my_list1)
bubble_sort(my_list1)
print(my_list1, "\n")
my_list2 = [random.randint(1, 100) for o in range(20)]
print(my_list2)
insertion_sort(my_list2)
print(my_list2)



