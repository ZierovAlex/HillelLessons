# В единственной строке записан текст. Для каждого слова из данного текста
# подсчитайте, сколько раз оно встречалось в этом тексте. Задачу необходимо
# решить с использованием словаря.

# Задаем текст в строку, переносим его по словам через пробел в список,
# из которого создаем словарь с ключами из слов заданного текста со значением
# None. Подставлем каждому ключу значение, количества ключей в заданном
# тексте.
# Выводим ответ по строчечно перебирая в цикле ключи и значения с помощью цикла.

entered_text = 'Не столь важно' \
               ' как медленно ты идешь' \
               ' как то' \
               ' как долго ты идешь' \
               ' не останавливаясь.'
entered_text = entered_text.lower()
entered_text = entered_text.split(' ')

working_dictionary = dict.fromkeys(entered_text)
for i in working_dictionary:
    working_dictionary[i] = entered_text.count(i)

print(working_dictionary)
for key, value in working_dictionary.items():
    print(f"Частица текста(слово) '{key}' в тексте встречается {value} раза")
