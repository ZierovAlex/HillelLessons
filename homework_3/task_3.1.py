# Написать програму для проверки пароля. У пользователя запрашивается пароль сравнивается с ожидаемой фразой - нужно сообщить о том что пароль совпал или пароль не совпал

password = input('Пожалуйста, задайте пароль!')
passowordcheck = input('Пожалуйста, введите пароль повторно для проверки!')

if password == passowordcheck:
    print('Пароль успешно подтвержден!')
else:
    print('Пароль не подтвержден! Запустите программу снова!')