integer = int(input('Пожалуйста, введите целое натуральное число!'))

for i in range(1, integer+1):
    a = str(i**2)
    b = str(i)
    if a[-len(b):] == b:
        print(i, '*', i, '=', i**2)
