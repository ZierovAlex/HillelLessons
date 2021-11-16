# # This is my first program
# print('Hi')
# # Trying to use commentary (получить только позитивные числа)
# # TODO: эта подсказка общепринята в разработке приложений,здесь мы обращаем внимание что и где нужно доделать или обратить внимание или откуда начать работу.
# integer = input('Введите целое число:')
# # TODO: команда TODO в коментарии создает вкладку внизу в пайчарме, в которой можно перемещаться между нашими туду.
# print(integer)  # комментарий "In line" или в строке(не более 4 слов или 80 символов  общепринято)
# ctrl + / добавляет в строки клеточку что бы превратить строку в комментарий
# value = 112
# # print("value:", value, "!")
# # print("value:" + "!")
# # del value # Операция по удалению переменной
# # print(value)

# var = input('num')
# var2 = int(var)
# print(var2 ** 2)
#
# var = int(input('num'))
# # # Функция eval() пытается выполнить переданный текст рассматривая его как кусок python кода
# txt = "(2+3)/0.25-4*2.1"
# print(txt, "=", eval(txt))

# v = "dwdcwcwcwc \n\t this is a test "
# print(v)


# a = b = c = 'spam'
# print(a,b,c)
# b = 'no'
# print(a,b,c)
#
# x, y = 2, 3 # структура "кортеж"
# # распаковка кортежа(позиционное присваивание)
# print(x,y)
#
# d,s,r = "123"
# print(d,s,r)
#
# z,m = x,y
# print(z,m)

# a = 12
# b = 10
# temp = a
# a = b
# b = temp
# print(a,b) # Замена местами переменных по питоновски

# x = 10
# y = 12
# print(x,y)
# x,y = y,x
# print(x,y) # Еще один вариант замены переменных

a = int(input())
b = int(input())
if a < b:
    print('Masliny Poimal')
else:
    print('Ti ubit')