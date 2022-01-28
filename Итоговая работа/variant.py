# Программа «Записная книжка»
# Код должен быть читаемым,  соотвествовать рекомендациям PEP8, с комментариями и соответствовать принципам DRY, KISS.
# Код должен быть загружен на GitHub или GitLab как отдельный проект с публичным доступом.
# Необходимо написать программу записную книжку.
# (Можно использовать элементы псевдографики)
#
# Каждая запись должна содержать поля:
# Имя*
# Фамилия*
# Номер телефона*
# Адрес
# Дата рождения
# Поля помеченные * обязательны к заполнению.
# Работа с записной книжкой должна осуществляться через набор текстовых, экранных меню. Выбор нужного пункта меню осуществляется с клавиатуры путем ввода номера пункта меню.
#
# В программе должны быть реализован следующий функционал:
# Добавление новой записи
# Удаление записи
# Редактирование записи
# Поиск по Имени
# Поиск по Номеру телефона
# (как дополнительное условие, не обязательное, дополнить возможность поиска по маске. Например, поиск записей по фамилии с применением маски: А*, должен вернуть все записи, у которых фамилия имеет в начале букву «А».
# 	Поиск должен быть регистро-независимым.)
# Сортировка по Имени
# Сортировка по Фамилии
# При выходе из программы сохранять все записи в файл
# При запуске программы проверять, если есть файл с данными, ранее сохранённый, то загрузить его в программу и сообщить о количестве загруженных записей.

# Пример меню:
#
# Добавить запись
# Удалить запись
# Изменить запись
# Поиск
# Сортировка

# Выход

from notebook import Notebook
from commands import Commands
import inp_check as ic

new_note = Notebook()

new_note.load_notebook()

nb_commands = Commands(new_note)

while True:
    print('-' * 20)
    print()
    new_note.print_note()
    print()
    nb_commands.notebook_commands()

    try:
        s = input('Выберите действие (номер команды от 0 до 6): ')

        if len(s.split(' ')) > 1:
            d = int(s.split(' ')[0])
            v = s.split(' ')[1]
        else:
            d = int(s.split(' ')[0])
            v = None

        if d == 0:
            new_note.print_record(int(v))
        elif d == 1:
            new_note.input_note()
        elif d == 2:
            new_note.delete_note(int(v))
        elif d == 3:
            new_note.edit_note(int(v))
        elif d == 4:
            search_what = input('Выберие по чему искать, "0" - по имени, '
                                '"1" - по фамилии, "2" - по номеру телефона: ')
            search_what = ic.check_input_search(search_what)
            output_text0 = 'Введите имя или первую букву имени для поиска: '
            output_text1 = 'Введите фвмилию или первую букву фамилии для ' \
                           'поиска: '
            output_text2 = 'Введите номер для поиска: '
            printed_text = ''
            if search_what == 0:
                printed_text = output_text0
            elif search_what == 1:
                printed_text = output_text1
            elif search_what == 2:
                printed_text = output_text2
            search_element = input(f"{printed_text}")
            search = new_note.search_note(search_what, search_element)
            for i in search:
                print(i)
            # TODO Реализовать поиск по первой букве и проверку на введенное в поиск
            #  если не находим то написать что искомый элемент не найден
        elif d == 5:
            sort_type = input('Введите "0" для сортировки по имени, "1" для '
                              'сортировки по фамилии: ')
            sort_type = ic.check_input_sort(sort_type)
            sort_direction = input('Введите "0" для сортировки по алфавиту, '
                                   '"1" для сортировки по алфавиту в '
                                   'обратном порядке: ')
            sort_direction = ic.check_sort_direction(sort_direction)
            if sort_direction == 0:
                new_note.sort_note(sort_type)
            elif sort_direction == 1:
                new_note.sort_note(sort_type, 'desc')
            # TODO Сделать всевозможные проверки на ввод данных!
            # TODO Добавить направление сортировки(изменить direct='asc')

        elif d == 6:
            new_note.save_notebook()
            break
        else:
            print('Такой команды нет')

    except Exception:
        print('Вы ввели неверную команду!')

#TODO добавить общение с пользоватетелм в коммандс отдельным методом