class Notebook:

    def __init__(self):
        self.notebook_list = []

    def load_notebook(self):
        import csv
        try:
            with open('notebook_save.csv', encoding='utf-8') as ns:
                self.notebook_list = list(csv.reader(ns))
            print(f"Загружено {len(self.notebook_list)} записей.")
            # csv_reader = csv.reader(ns)
            # for row in csv_reader:
            #     self.notebook_list.append(row)

        except Exception:
            print('Сохраненные записи отсутствуют!')

    # CSV файл

    def input_note(self):
        import inp_check as check

        name = input('Введите имя: ')
        name = check.empty_check(name)
        # name = check.string_from_input(name)
        surname = input('Введите фамилию: ')
        surname = check.empty_check(surname)
        # surname = check.string_from_input(surname)
        telephone_number = input('Введите номер телефона: ')
        telephone_number = check.number_check(telephone_number)
        address = input('Введите адрес: ')
        date_of_birth = input('Введите дату рождения в формате ДД.ММ.ГГГГ: ')
        date_of_birth = check.date_check(date_of_birth)
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

    # def edit_note(self, note_id, name, surname, telephone_number, address,
    #               date_of_birth):
    #     self.notebook_list[note_id] = [name, surname, telephone_number,
    #     address, date_of_birth]
    def edit_note(self, note_id):
        import inp_check as check

        name = input('Введите имя: ')
        name = check.empty_check(name)
        # name = check.string_from_input(name)
        surname = input('Введите фамилию: ')
        surname = check.empty_check(surname)
        # surname = check.string_from_input(surname)
        telephone_number = input('Введите номер телефона: ')
        telephone_number = check.number_check(telephone_number)
        address = input('Введите адрес: ')
        date_of_birth = input('Введите дату рождения в формате ДД.ММ.ГГГГ: ')
        date_of_birth = check.date_check(date_of_birth)
        self.notebook_list[note_id] = [name, surname, telephone_number, address,
                                       date_of_birth]

    def search_note(self, id, search_fragment):
        if len(search_fragment) == 1:
            for row in self.notebook_list:
                if search_fragment == row[id][0]:
                    yield row
        else:
            for record in self.notebook_list:
                if search_fragment in record[id]:
                    yield record
        # for i in range(len(self.notebook_list)):
        #     if search_fragment == self.notebook_list[i][id]:
        #         yield self.notebook_list[i]

    def sort_note(self, id, direct='asc'):
        n = len(self.notebook_list)
        # Внешний цикл кол-во проходов n-1
        for i in range(n - 1):
            # Внутренний цикл проходим от n - 2 до i - 1 проходов двигаясь с
            # конца
            for j in range(n - 2, i - 1, -1):
                # Меняем элементы местами
                if (self.notebook_list[j + 1][id] < self.notebook_list[j][
                        id]) != (direct == 'desc'):
                    self.notebook_list[j], self.notebook_list[j + 1] = \
                        self.notebook_list[j + 1], self.notebook_list[j]
        # print(self.notebook_list)

    def save_notebook(self):
        import csv
        with open('notebook_save.csv', 'w', encoding='utf-8',
                  newline='') as save:
            save_notebook = csv.writer(save)
            for row in self.notebook_list:
                save_notebook.writerow(row)

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


if __name__ == "__main__":
    n = Notebook()
