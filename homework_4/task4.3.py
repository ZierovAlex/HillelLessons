# Ввести натуральное число и определить, верно ли, что в его записи есть 2 одинаковые цифры стоящие рядом.

input_number = input('Введите целое число!')
cnt = 0

for i in input_number:
    if i == input_number[cnt+1]:
        print('Да, есть одинаковые цифры стоящие рядом!')
        break
    cnt += 1
    if cnt == len(input_number) - 1:
        print('Нет стоящих рядом одинаковых цифр!')
        break

