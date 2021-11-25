input_string = input('Please enter two words separated by a "space"!')
input_string = input_string.lower()
word1 = ''
word2 = ''

# Словом в этой программе считается сочитание как иминимум 2х букв.

while True:
    if input_string.count(' ') == 1 and input_string.find(' ') > 1:
        if input_string[:input_string.find(' ')].isalpha() and input_string[input_string.find(' ')+1:].isalpha():
            word1 += input_string[:input_string.find(' ')]
            word2 += input_string[input_string.find(' ')+1:]
            if len(word1) > 1 and len(word2) > 1:
                word1, word2 = word1[::-1], word2[::-1]
                word1 = word1[0].upper() + word1[1:]
                word2 = word2[0].upper() + word2[1:]
                print(word1, word2)
                break
    input_string = input('Please, enter words correctly and use "space"!')
    input_string = input_string.lower()
