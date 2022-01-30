# def check_input_commands(n, c):
#     n = str(n)
#     while True:
#         if n.isdigit():
#             n = int(n)
#             if c > n >= 0:
#                 break
#             else:
#                 n = input('Некорректный номер, попробуйте еще раз: ')
#         else:
#             n = input('Некорректный ввод, попробуйте еще раз: ')
#     return n
#
# def check_record_number(n, notebook):
#     n = str(n)
#     while True:
#         if n.isdigit():
#             n = int(n)
#             try:
#                 if notebook.is_show(n):
#                     break
#                 else:
#                     n = input('Некорректный номер, попробуйте еще раз: ')
#             except Exception:
#                 n = input('Некорректный номер, попробуйте еще раз: ')
#         else:
#             n = input('Некорректный ввод, попробуйте еще раз: ')
#     return n


def check_input_sort(n):
    n = str(n)
    while True:
        if n.isdigit():
            n = int(n)
            if 1 >= n >= 0:
                break
            else:
                n = input('Введена несуществующая команда, введите "0" для '
                          'сортировки по имени, "1" для сортировки по '
                          'фамилии: ')
        else:
            n = input('Введено некорректно, введите "0" для сортировки по '
                      'имени, "1" для сортировки по фамилии: ')
    return n


def check_sort_direction(n):
    n = str(n)
    while True:
        if n.isdigit():
            n = int(n)
            if 1 >= n >= 0:
                break
            else:
                n = input('Введена несуществующая команда, введите "0" для '
                          'сортировки по алфавиту, "1" для сортировки по '
                          'алфавиту в обратном порядке: ')
        else:
            n = input('Введено некорректно, введите "0" для сортировки по '
                      'алфавиту, "1" для сортировки по алфавиту в обратном '
                      'порядке: ')
    return n


def string_from_input(n):
    n = str(n)
    while True:
        if n.isalpha():
            n = str(n)
            break
        else:
            n = input('Введено некорректно, пожалуйста попробуйте еще раз: ')

    return n


def number_check(n):
    n = str(n)
    while True:
        if n == '':
            n = input("Вы ввели пустую строку, это поле обязательно к "
                      "заполнению: ")
        elif not (n.isnumeric()):
            n = input('Введено некорректно, пожалуйста попробуйте еще раз: ')
        else:
            n = str(n)
            break

    return n


def date_check(n):
    n = str(n)
    while True:
        if (n[:2].isnumeric() and n[2] == '.' and n[3:5].isnumeric() and n[5]
                == '.' and n[6:10].isnumeric()) or n == '':
            break
        else:
            n = input('Введено некорректно пожалуйста ввежите дату в формате '
                      'ДД.ММ.ГГГГ')
    return n


def empty_check(n):
    n = str(n)
    while True:
        if n != '':
            break
        else:
            n = input('Вы ввели пустую строку, это поле обязательно к '
                      'заполнению: ')

    return n


# def integer_from_input() -> int:
#     n: int = 0
#
#     while True:
#         str_n = input('Input your integer:')
#         if str_n.isnumeric():
#             n = int(str_n)
#             break
#         else:
#             print('Input is not correct please try again')
#
#     return n


if __name__ == "__main__":
    # a = integer_from_input()
    str_from_inp = 'Alex'
    int_in_str = '0987'
    my_date = '17.07.1992'
    string_from_input(str_from_inp)
    number_check(int_in_str)
    date_check(my_date)
