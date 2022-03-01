class ListChecker:
    def __init__(self):
        self.my_list = []

    def __str__(self):
        return str(self.my_list)

    def append_value(self):
        state = 'y'
        while True:
            if state == 'n':
                break
            elif state not in ('y', 'n'):
                state = input('Попробуете ещё раз. y/n (Да/Нет): ')
            elif state == 'y':
                try:
                    value = input('Введите значение: ')
                    if isinstance(float(value), float) or isinstance(int(value), int):
                        self.my_list.append(value)
                except ValueError:
                    print(f'Ошибка добавления')
                state = input('Добавить значение? y/n  (Да/Нет): ')


if __name__ == '__main__':
    lst_nums = ListChecker()
    lst_nums.append_value()
    print(lst_nums)