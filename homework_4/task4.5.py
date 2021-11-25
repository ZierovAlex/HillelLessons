inp_string = input('Пожалуйста, задайте строку для последующего поиска в ней нужного элемента!')
inp_char = input('Пожалуйста, задайте искомый элемент строки!')
a = 0
b = 0
count = ''
if inp_char in inp_string:
    while True:
        b = inp_string.find(inp_char, a+1)
        a = b
        if b == -1:
            break
        count += str(b)+' '
    print('Символ "inp_char" в строке "inp_string" находится на позициях(индекс):', count)
else:
    print('Элемент "inp_char" отсутствует в заданной строке "inp_string"')
