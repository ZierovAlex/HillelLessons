class Notebook:

    def __init__(self):
        self.notebook_list = []

    @staticmethod
    def date_check(date):
        date = str(date)
        while True:
            if (date[:2].isnumeric() and date[2] == '.' and date[
                                                            3:5].isnumeric() and
                date[5] == '.' and date[
                                   6:10].isnumeric()) or date == '':
                break
            else:
                date = input(
                    'Введено некорректно пожалуйста ввежите дату в формате '
                    'ДД.ММ.ГГГГ')
        return date

    @staticmethod
    def number_check(telephone_number):
        telephone_number = str(telephone_number)
        while True:
            if telephone_number == '':
                telephone_number = input("Вы ввели пустую строку, это поле"
                                         " обязательно к заполнению: ")
            elif not (telephone_number.isnumeric()):
                telephone_number = input(
                    'Введено некорректно, пожалуйста попробуйте еще раз: ')
            else:
                telephone_number = str(telephone_number)
                break

        return telephone_number

    @staticmethod
    def empty_check(check_element):
        check_element = str(check_element)
        while True:
            if check_element != '':
                break
            else:
                check_element = input('Вы ввели пустую строку, это поле'
                                      ' обязательно к заполнению: ')

        return check_element

    def load_notebook(self):
        import csv
        try:
            with open('notebook_save.csv', encoding='utf-8') as ns:
                self.notebook_list = list(csv.reader(ns))
            for record in self.notebook_list:
                record[5] = bool(record[5])
            print(f"Загружено {len(self.notebook_list)} записей.")  # add

        except Exception:
            print('Сохраненные записи отсутствуют!')

    def input_note(self):
        name = input('Введите имя: ')
        name = self.empty_check(name)
        surname = input('Введите фамилию: ')
        surname = self.empty_check(surname)
        telephone_number = input('Введите номер телефона: ')
        telephone_number = self.number_check(telephone_number)
        address = input('Введите адрес: ')
        date_of_birth = input('Введите дату рождения в формате ДД.ММ.ГГГГ: ')
        date_of_birth = self.date_check(date_of_birth)
        self.add_note(name, surname, telephone_number, address, date_of_birth)

    # TODO Обьеденить инпут ноут и эдд ноут(эдд используется только в инпут

    def add_note(self, name, surname, telephone_number, address, date_of_birth):
        note = [name, surname, telephone_number, address, date_of_birth, True]
        self.notebook_list.append(note)

    def delete_note(self, note_id):
        try:
            self.notebook_list.pop(note_id)
        except Exception:
            print('Удаляемый элемент не найден!')

    def edit_note(self, note_id):
        record = self.notebook_list[note_id]
        # TODO ПРОПИСАТЬ ВСЕ СТРОКИ КАК НЭЙМ ЭТО ДЛЯ ТОГО ЧТО БЫ ПРИ ВВОДЕ
        #  ПУСТОЙ СТРОКИ ДАННЫЙ НЕ МЕНЯЛИСЬ, последние 2 строчки они не нужны
        #  ДОБАВИТЬ
        print(f'Текущее имя: {record[0]}')
        name = input('Введите имя: ')
        if name != '':
            record[0] = self.empty_check(name)
        surname = input('Введите фамилию: ')
        surname = self.empty_check(surname)

        telephone_number = input('Введите номер телефона: ')
        telephone_number = self.number_check(telephone_number)
        address = input('Введите адрес: ')
        date_of_birth = input('Введите дату рождения в формате ДД.ММ.ГГГГ: ')
        date_of_birth = self.date_check(date_of_birth)
        self.notebook_list[note_id] = [name, surname, telephone_number, address,
                                       date_of_birth, True]

    def search_note(self, id, search_fragment):
        search_fragment = search_fragment.lower()
        count = 0
        for record in self.notebook_list:
            text = record[id].lower()
            if ((search_fragment[0] == '*') and (text.endswith(search_fragment[
                                                               1:]))) or (
                    (search_fragment[-1] == '*') & (text.startswith(
                search_fragment[:-1]))) or (('*' not in search_fragment)
                                            and (search_fragment in text)):
                record[5] = True
                count = count + 1
            else:
                record[5] = False
        return count

    def show_all(self):
        for record in self.notebook_list:
            record[5] = True

    def is_show(self, id):

        return self.notebook_list[id][5]

    def sort_note(self, id, direct='asc'):
        records = len(self.notebook_list)
        for i in range(records - 1):
            for j in range(records - 2, i - 1, -1):
                if (self.notebook_list[j + 1][id] < self.notebook_list[j][
                        id]) != (direct == 'desc'):
                    self.notebook_list[j], self.notebook_list[j + 1] = \
                        self.notebook_list[j + 1], self.notebook_list[j]

    def save_notebook(self):
        import csv
        with open('notebook_save.csv', 'w', encoding='utf-8',
                  newline='') as save:
            save_notebook = csv.writer(save)
            for row in self.notebook_list:
                save_notebook.writerow(row)

    def print_note(self):  # TODO ПЕРЕИМЕНОВАТЬ НА SHOW ALL RECORDS
        for i in range(len(self.notebook_list)):
            if self.notebook_list[i][5]:  # add
                print(i, self.notebook_list[i][0], self.notebook_list[i][1],
                      sep='\t')

    def print_record(self, record_id):  # TODO ПЕРЕИМЕНОВАТЬ НА SHOW RECORD
        print('name:', self.notebook_list[record_id][0], sep='\t')
        print('surname:', self.notebook_list[record_id][1], sep='\t')
        print('telephone number:', self.notebook_list[record_id][2], sep='\t')
        print('address:', self.notebook_list[record_id][3], sep='\t')
        print('date of birth:', self.notebook_list[record_id][4], sep='\t')

    def notebook_size(self):
        return len(self.notebook_list)


if __name__ == "__main__":
    n = Notebook()
