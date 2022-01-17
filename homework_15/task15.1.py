with open('file1.txt', 'w', encoding='utf-8') as file:

    while True:
        a = input()
        if a == '':
            break
        else:
            file.writelines(a + '\n')

