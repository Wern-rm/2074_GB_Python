__author__ = 'Roman Morozov'


def transform_string(number: int) -> str:
    """
    Возвращает строку вида 'N процентов' с учётом склонения по указанному number
    :param number:
    :return:
    """
    next_str: str = f"{number + 1}"
    if int(next_str[-1]) == 1 and number + 1 != 11:
        return f"{next_str} Процент"
    elif 1 < int(next_str[-1]) <= 4:
        if 10 < number + 1 <= 14:
            return f"{next_str} Процентов"
        else:
            return f"{next_str} Процента"
    else:
        return f"{next_str} Процентов"


if __name__ == '__main__':
    for i in range(100):
        print(transform_string(number=i))