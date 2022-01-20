__author__ = 'Roman Morozov'


def convert_list_in_str(list_in: list) -> str:
    # a
    sort_list: list = list_in[::-1]

    for i in sort_list:
        if sort_list[sort_list.index(i)].isdigit() is True and sort_list[sort_list.index(i)].startswith('"') is False:
            sort_list.insert(sort_list.index(i) + 1, '"')
        elif sort_list[sort_list.index(i)].isdigit() is False and sort_list[sort_list.index(i)].startswith('+') is True:
            sort_list.insert(sort_list.index(i) + 1, '"')
    # b
    sort_list = sort_list[::-1]

    for i in sort_list:
        if sort_list[sort_list.index(i)].isdigit() is True and sort_list[sort_list.index(i)].startswith('"') is False:
            sort_list.insert(sort_list.index(i) + 1, '"')
            if len(i) == 1:
                sort_list[sort_list.index(i)] = '0' + i

        elif sort_list[sort_list.index(i)].isdigit() is False and sort_list[sort_list.index(i)].startswith('+') is True:
            sort_list.insert(sort_list.index(i) + 1, '"')

    return ' '.join(sort_list)


if __name__ == '__main__':
    my_list: list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
    result: str = convert_list_in_str(my_list)
    print(result)