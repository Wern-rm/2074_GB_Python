__author__ = 'Roman Morozov'


def convert_name_extract(list_in: list) -> list:
    tmp: list = []
    for i in list_in:
        i = i.title()
        name = i.rpartition(' ')
        tmp.append(f'Привет, {name[-1]}!')
    return tmp


if __name__ == '__main__':
    example_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
    result = convert_name_extract(example_list)
    print(result)