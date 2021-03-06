# Реализовать приложение которое принимает на вход значение чисел от 3 до 9;
# Выполняет проверку на правильность введеного числа в указаном диапазоне.
# Если не в диапазоне - сообщает о проблеме и заканчивает работу.
# Иначе - печатает пирамиду из чисел.

# Задаём переменные: для пользовательского ввода (inp_number), счетчик (count),
# (result) для отображения пирамиды

inp_number = input('Input number from 3 to 9:')
count = 1
result = ''

# Выполняем проверку на правильность введеного числа в указаном диапазоне
# используя условные операторы if и else
# Если результат "True", выполняется цикл while в котором цикл for формирует
# переменную result с каждой итерацией while.
# "Print" поочередно выводит строки в "Run" с каждой итерацией цикла while,
# формируя пирамиду.
# Увеличиваем значение count на единицу он участвует в реализации for и
# возвращаем исходное значение result.
# Ограничиваем цикл while сравнивая его со счетчиком count после выведения
# последней строки пирамиды.


if inp_number.isdigit():
    inp_number = int(inp_number)
    if 3 <= inp_number <= 9:
        print('You entered correctly!')
        while True:
            for i in range(1, count+1):
                result += str(i)
            print(f"{result}{result[-2::-1]}")
            count += 1
            result = ''
            if count == inp_number+1:
                break
    else:
        print('You entered incorrect data, program error!')
else:
    print('You entered incorrect data, program error!')
