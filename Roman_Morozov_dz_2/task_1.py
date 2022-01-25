__author__ = 'Roman Morozov'


def task() -> None:
    """
    1. Выяснить тип результата выражений:
    :param duration:
    :return:
    """
    print(type(15 * 3))
    print(type(15 / 3))
    print(type(15 // 2))
    print(type(15 ** 2))
    print(type(15 % 2))


if __name__ == '__main__':
    task()