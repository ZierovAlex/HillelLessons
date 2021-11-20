# Задача на опеределение високосного года.
# n.isdigit - позволяет проверить, являются ли символы, из которых состоит строка цифрами. С помощью этого метода мы можем проверить, записано ли в строку целое положительное число или нет. Положительное — это потому, что знак минус не будет считаться цифрой и метод вернет значение False.

yearcheck = input('Please, enter the year you want to check if it is a leap year or not!')

if yearcheck.isdigit():
    yearcheck = int(yearcheck)
    if 1900 <= yearcheck <= 1000000:
        if (yearcheck % 4 == 0 and yearcheck % 100 != 0) or (yearcheck % 400 == 0):
            print(yearcheck, 'is a leap year')
        else:
            print(yearcheck, 'is not leap year')
    else:
        print('Invalid data entered, please run the program again and enter the correct value, from 1900 to 1000000!')
else:
    print('"',yearcheck,'"', 'is not a year, please run program again and enter the correct value!')
