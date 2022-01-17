def longest_words(file):
    list_text_atricle = ''
    for row in file:
        for letter in row:
            if letter == "\n":
                letter = " "
            list_text_atricle += letter

    list_text_atricle = list_text_atricle.lower().split(' ')
    list_of_longest_words = []
    longest_word = max(list_text_atricle, key=len)
    for i in list_text_atricle:
        if len(i) == len(longest_word) and i != longest_word:
            list_of_longest_words.append(i)
    list_of_longest_words.append(longest_word)
    return list_of_longest_words


with open('article.txt', 'r', encoding='utf-8') as art:
    print("Самые длинные слово(а) в тексте:", *longest_words(art))
