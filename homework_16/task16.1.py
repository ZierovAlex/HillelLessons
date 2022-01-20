# Реализовать класс цифрового счетчика.
# Обеспечьте возможность:
# установки максимального и минимального значений (счетчик считает от меньшего
# к большему)
# увеличения счетчика на 1 (инкремент). Метод который инкрементирует счетчик
# возращает его значение.
# при достижении максимума ( при переполнении счетчика) увеличения не
# происходит.
# метода который реализует получение значения счетчика.
# метод сброса счетчика в начальное (минимальное) значение


class DigitalCounter:

    # Устанавливаем атрибуты в конструкторе: текущее значени, минимальное и
    # максимальное значение счетчика
    def __init__(self):
        self.current_value = 0
        self.minvalue = 0
        self.maxvalue = 10

    def set_min_value(self, setmin):
        if self.minvalue < self.maxvalue:
            self.minvalue = setmin
            self.current_value = self.minvalue
        else:
            print('Error! Minimum value cannot be greater than Maximum value')

    def set_max_value(self, setmax):
        if self.maxvalue > self.minvalue:
            self.maxvalue = setmax
        else:
            print("Error! Maximum value cannot be lesser than Minimum value:")

    # Увеличиваем значение счетчика на 1 инкремент по умолчанию и возвращаем
    # его значение (return)
    def increase(self, increment=1):
        # Устанавливаем условие при котором счетчик перестанет увеличиватся
        # при достижении максимального значения
        if self.current_value + increment <= self.maxvalue:
            self.current_value = self.current_value + increment
        else:
            print('The counter has reached maximum')
        return self.current_value

    # Метод который дает информацию о текущем состоянии счетчика: текущее
    # значение(по условию) а так же установленные минимальные и максимальные
    # значения счетчика
    def get_info(self):
        print(f"Текущее значение счетчика: {self.current_value}")
        print(f"Минимальное значение счетчика: {self.minvalue}")
        print(f"Максимальное значение счетчика: {self.maxvalue}")

    # Метод сброса счетчика к умтановленному минимальному значению
    def reset_counter(self):
        self.current_value = self.minvalue


my_counter = DigitalCounter()

my_counter.set_max_value(3)
my_counter.increase()
my_counter.increase()
my_counter.get_info()
my_counter.increase()
my_counter.increase()
my_counter.get_info()
my_counter.reset_counter()
my_counter.get_info()
