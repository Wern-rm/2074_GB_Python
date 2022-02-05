'''
Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
Подумайте: полезен ли будет вам оператор распаковки? Как поступить,
если потребуется сортировка по ключам? Можно ли использовать словарь в этом случае?
'''


def thesaurus(names: list[str]) -> dict:
    dict_out: dict = {}
    for i in names:
        if i[0] in dict_out.keys():
            dict_out[i[0]] += [i]
        else:
            dict_out[i[0]] = [i]
    return dict(sorted(dict_out.items()))


def thesaurus_adv(names: list[str]) -> dict:
    dict_out: dict = {}
    for i in names:
        text = i[i.rfind(' '):]
        if text[1] in dict_out.keys():
            dict_out[text[1]] += [i]
        else:
            dict_out[text[1]] = [i]
    for j in dict_out.keys():
        dict_out[j] = thesaurus(dict_out[j])
    return dict(sorted(dict_out.items()))


if __name__ == '__main__':
    print(thesaurus(["Иван", "Мария", "Петр", "Илья", "Сергей", "Роман", "Евгений", "Артем"]))
    print('-------------------')
    print(thesaurus_adv(["Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева", "Роман Морозов"]))
