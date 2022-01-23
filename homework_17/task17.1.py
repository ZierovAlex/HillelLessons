# Вам на вход приходит последовательность целых чисел. Вам надо обрабатывать
# ее следующим образом: выводить на экран сумму первых пяти чисел этой
# последовательности, затем следующих 5 итд Но последовательность не дается
# вам сразу целиком. С течением времени к вам поступают ещё последовательные
# части. Например, сначала первые три элемента, потом следующие шесть,
# потом следующие два и т. д.
#
# Реализуйте класс Buffer, который будет накапливать в себе элементы
# последовательности и выводить сумму пятерок последовательных элементов по
# мере их накопления.
#
# Одним из требований к классу является то, что он не должен хранить в себе
# больше элементов, чем ему действительно необходимо, т. е. он не должен
# хранить элементы, которые уже вошли в пятерку, для которой была выведена
# сумма.
#
# Класс должен иметь следующий вид
#
#
# class Buffer:
#
#     def __init__(self):
#          # конструктор без аргументов
#          pass
#
#     def add(self, *a):
#         # добавить следующую часть последовательности
#         pass
#
#     def get_current_part(self):
#         # вернуть сохраненные в текущий момент элементы последовательности
#         # в порядке, в котором они были добавлены
#         pass

class Buffer:
    my_list = []
    last_input = tuple()

    def __init__(self):
        pass

    @classmethod
    def add(cls, *a):
        cls.last_input = a
        for i in cls.last_input:
            cls.my_list.append(i)
            if len(cls.my_list) == 5:
                print(f"Accumulated 5 numbers, their sum: {sum(cls.my_list)}")
                cls.my_list.clear()
        print(f"Remaining accumulated numbers: {cls.my_list}")

    @classmethod
    def get_current_par(cls):
        print(f"Last time you entered:*{cls.last_input}")


example = Buffer()

example.add(10, 22, 1, 100, 22, 55, 83, 10, 55)
example.get_current_par()
example.add(89, 7, 66, 100)
example.get_current_par()
example.add(10, 22, 1, 100, 22, 55, 83, 10, 55)
example.get_current_par()
example.add(10, 22, 1, 100, 22, 55, 83, 10, 55, 100, 300, 99, 44, 76, 12)
example.get_current_par()