from homework_13.task13_2 import input_check as check


class TooShortNameExeption(Exception):
    def __init__(self, value):
        self.msg = value

    def __str__(self):
        return f"Ошибка: {self.msg}"


while True:
    try:
        my_name = check.string_from_input()
        if len(my_name) < 3:
            raise TooShortNameExeption("Введенное имя слишком короткое имя")
    except TooShortNameExeption as tsne:
        print(tsne)
    else:
        print(my_name)
        break
