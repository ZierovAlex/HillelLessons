def my_first_try(input1, input2):
    try:
        input1 = int(input1)
        input2 = int(input2)
    except ValueError:
        input1 = str(input1)
        input2 = str(input2)
        my_summ = input1 + input2
        return my_summ
    else:
        my_summ1 = input1 + input2
        return my_summ1


print("Сумма введеных данных:", my_first_try(input("Введите первое число:"),
                                             input("Введите "
                                                   "второе "
                                                   "число:")))
