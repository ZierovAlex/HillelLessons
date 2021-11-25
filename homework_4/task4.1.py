# Ввести натуральное число и определить, верно ли, что в его записи есть две одинаковые цифры(не обязательно рядом)

number = input('Введите натуральное число!')
cnt = 0

while cnt < len(number):
    if number.count(number[cnt]) > 1:
        print('Да. есть повтор!')
        break
    elif number.count(number[cnt]) == 1:
        cnt += 1
else:
    print('Нет повтора!')

# Пришло в голову более простое решение с помощью цикла for

for n in number:
    if number.count(n) > 1:
        print('Yes')
        break
else:
    print('No')