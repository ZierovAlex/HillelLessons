# my_list = [1, 2, [1, 5, 10], '21212']
# for i in my_list:
#     print(f"{i} - {type(i)}")
#
# Программа которая запрашивает у пользователья 5 раз значене и добавляет в список

lst = list()

for a in range(5):
    a = input('input string please:')
    lst.append(a)

print(lst)
