# # Баги и ошибки
#
# try:
#     try:
#         x = 1 / 0
#     except NameError:
#         print("Неопределенный Индетификатор")
#     except IndexError:
#         print("Несущ индекс")
#     print('After try')
# except ZeroDivisionError:
#     print('Обработка деления на ноль')
#     x = 0
#
# print(x)
#
# class MyError(Exception):
#     def __init__(self, value):
#         self.msg = value
#
#     def __

# fid = open("lol.txt", "r")
# print(fid.read())

fid = open("lol.txt", "r")
print(fid.read())
