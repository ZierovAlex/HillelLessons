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

class Notebook:

    def __init__(self):
        self.notebook_list = []

    def load_notebook(self):
        pass
    # CSV файл

    def input_note(self):
        name = input('Введите имя: ')
        surname = input('Введите фамилию: ')
        telephone_number = input('Введите номер телефона: ')
        address = input('Введите адрес: ')
        date_of_birth = input('Введите дату рождения: ')
        self.add_note(name, surname, telephone_number, address, date_of_birth)

    def add_note(self, name, surname, telephone_number, address, date_of_birth):
        note = [name, surname, telephone_number, address, date_of_birth]
        self.notebook_list.append(note)
        # print(self.notebook_list)

    def delete_note(self, note_id):
        try:
            self.notebook_list.pop(note_id)
        except Exception:
            print('id is not found, please check id')
        # print(self.notebook_list)

    def edit_note(self, note_id, name, surname, telephone_number, address, date_of_birth):
        self.notebook_list[note_id] = [name, surname, telephone_number, address, date_of_birth]

    def search_note(self, id, search_fragment):
        # for i in range(len(self.notebook_list)):
        #     if search_fragment == self.notebook_list[i][id]:
        #         yield self.notebook_list[i]
        for record in self.notebook_list:
            if search_fragment in record[id]:
                yield record


    def sort_note(self, id, direct='asc'):
        n = len(self.notebook_list)
        # Внешний цикл кол-во проходов n-1
        for i in range(n - 1):
            # Внутренний цикл проходим от n - 2 до i - 1 проходов двигаясь с конца
            for j in range(n - 2, i - 1, -1):
                # Меняем элементы местами
                if (self.notebook_list[j + 1][id] < self.notebook_list[j][
                    id]) != (direct=='desc'):
                    self.notebook_list[j], self.notebook_list[j + 1] = self.notebook_list[j + 1], self.notebook_list[j]
        # print(self.notebook_list)

    def save_notebook(self):
        pass

    def print_note(self):
        for i in range(len(self.notebook_list)):
            print(i, self.notebook_list[i][0], self.notebook_list[i][1],
                  sep='\t')

    def print_record(self, record_id):
        print('name:', self.notebook_list[record_id][0], sep='\t')
        print('surname:', self.notebook_list[record_id][1], sep='\t')
        print('telephone number:', self.notebook_list[record_id][2], sep='\t')
        print('address:', self.notebook_list[record_id][3], sep='\t')
        print('date of birth:', self.notebook_list[record_id][4], sep='\t')

new_note = Notebook()

new_note.add_note('Alex', 'Ziirov', '067463735', 'Hrushevskogo str.',
                  '17.07.1992')
new_note.add_note('Dmitri', 'Belik', '000000000', 'Rihtera str.',
                  '02.04.1992')
new_note.add_note('Неизвестный', 'Чикатило', '7777777777', 'Ростов',
                  '1930')

while True:
    print('-' * 20)
    print()
    new_note.print_note()
    print()
    print('Действия')
    print('0 Просмотреть ("номер действия" "номер записи которую хотите '
          'просмотреть" )')
    print('1 Добавить')
    print('2 Удалить')
    print('3 Изменить')
    print('4 Поиск')
    print('5 Сортировать')
    print('6 Выход')
    s = input('Выберите действие:')
    print('-' * 20)
    print()
#
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
        pass
    elif d == 4:
        search = new_note.search_note(0, v)
        for i in search:
            print(i)
    elif d == 5:
        if v is None:
            new_note.sort_note(0)
        else:
            new_note.sort_note(0, v)
    elif d == 6:
        break
    else:
        print('Такой команды нет')
