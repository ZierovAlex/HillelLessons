# Дан список целых чисел (можно сгенерировать при помощи генератора случайных
# чисел), число k и значение C. Необходимо вставить в список на позицию с
# индексом k значение C, сдвинув все элементы, с индексом большим k, вправо.
# Поскольку при этом количество элементов в списке увеличивается, в конец
# списка нужно будет добавить новый элемент (любое значение),
# используя метод append(). Вставку необходимо осуществлять уже в считанном
# списке, не делая этого при выводе и не создавая дополнительного списка.
# Использовать метод insert() не разрешается.

# Генерируем список и присваеваем его переменной input_list
# Генерируем переменную element_index для ввода позиции(индекса) "k"
# Создаем переменную element_C котора содержит значенме "C"
# Создаем счетчик count

import random
input_list = [random.randint(10, 100) for i in range(10)]
print(f"Генерируем список из случайных числел: {input_list}")
element_index = random.randint(0, 10)
print(f"Задаем случайный индекс элемента списка для операции: {element_index}")
element_C = random.randint(101, 1000)
print(f"Задаем случайное значение 'element_C' для операции: {element_C}")
count = -1

# Делаем проверку на тот случай если нужно вставить элемент в конец списка и
# если это так то просто добавляем обьект "element_C" в конец:

if element_index == len(input_list):
    input_list.append(element_C)
    print(
        f"'element_C' со значением {element_C} вставлен в список 'input_list'"
        f" на позицию с индексом {element_index}: {input_list}"
    )

# В остальных случаях вносим значение "element_С" в список и перемещаем его по
# списку в нужное место c индексом "element_index":

else:
    input_list.append(element_C)
    while True:
        input_list[count], input_list[count-1] = input_list[count-1],\
            input_list[count]
        count -= 1
        if input_list.index(element_C) == element_index:
            break
    print(
        f"'element_C' со значением {element_C} вставлен в список 'input_list'"
        f" на позицию с индексом {element_index}: {input_list}"
    )
