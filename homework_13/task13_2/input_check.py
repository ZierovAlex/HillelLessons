__all__ = ["integer_from_input", "string_from_input", "two_words_sep_space"]


def integer_from_input() -> int:
    n: int = 0

    while True:
        str_n = input('Input your integer:')
        if str_n.isnumeric():
            n = int(str_n)
            break
        else:
            print('Input is not correct please try again')

    return n


def string_from_input():
    while True:
        n = input('Пожалуйста введите имя!')

        if n.isalpha():
            n = str(n)
            break
        else:
            print('Input is not correct please try again')

    return n


def two_words_sep_space():
    """Проверка что введены именно два слова разделенные пробелом без чисел и
    символов """

    # Словом в этой программе считается сочитание как иминимум 2х букв.

    while True:
        input_string = input('Please enter two words with space:')
        input_string = input_string.lower()
        word1 = ''
        word2 = ''
        if input_string.count(' ') == 1 and input_string.find(' ') > 1:
            if input_string[:input_string.find(' ')].isalpha() and input_string[
                input_string.find(
                    ' ') + 1:].isalpha():
                word1 += input_string[:input_string.find(' ')]
                word2 += input_string[input_string.find(' ') + 1:]

                if len(word1) > 1 and len(word2) > 1:
                    return input_string
                else:
                    print('Please, enter words correctly and use "space"!')
            else:
                print('Please, enter words correctly and use "space"!')
        else:
            print('Please, enter words correctly and use "space"!')


if __name__ == "__main__":
    a = integer_from_input()
    b = string_from_input()
    c = two_words_sep_space()
