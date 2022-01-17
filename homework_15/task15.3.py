def update_hero(**kwargs):
    argment_dict = kwargs
    with open('hero.ini', 'r', encoding='utf-8') as hero_ini:
        my_dict = {}
        for row in hero_ini:
            splitted_row = row.split('=')
            my_dict[splitted_row[0]] = splitted_row[1].replace('\n', '')
        for key, value in argment_dict.items():
            my_dict[key] = value
    with open('hero.ini', 'w', encoding='utf-8') as hero_ini:
        for key, value in my_dict.items():
            row = key + '=' + value + '\n'
            hero_ini.write(row)


update_hero(
    hero=input('Input hero name:'), power=input('Input hero power('
                                                'integer):'),
    alive=input('Hero status "True" of "False":'),
    speed=input('Input hero speed(integer):'), X=input('Input hero height('
                                                       '1.0):'),
    Y=input('Input hero width(1.0):')
)
