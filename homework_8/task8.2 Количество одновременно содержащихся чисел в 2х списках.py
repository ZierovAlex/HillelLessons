# Даны два списка чисел. Посчитайте, сколько чисел содержится одновременно как
# в первом списке, так и во втором. Эту задачу на python можно решить в одну
# строчку.

import random

list_1 = [random.randint(0, 25) for i in range(10)]
print(list_1)
list_2 = [random.randint(0, 25) for j in range(10)]
print(list_2)

# Решаем в одну строчку

print(f"Количество одновременно содержащихся элементов в двух списках: "
      f"{len(set(list_2) & set(list_1))}")
