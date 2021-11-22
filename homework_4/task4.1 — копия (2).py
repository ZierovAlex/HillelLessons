input_number = input('Введите целое число!')
cnt = 0

for i in input_number:
    if i == input_number[cnt+1]:
        print('Да')
        break
    cnt += 1
    if cnt == len(input_number) - 1:
        print('Нет')
        break

