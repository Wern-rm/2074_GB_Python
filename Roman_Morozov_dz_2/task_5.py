__author__ = 'Roman Morozov'


def task_a(price_list: list) -> str:
    result: list = []
    for i in price_list:
        if type(price_list[price_list.index(i)]) == float:
            r, k = str(price_list[price_list.index(i)]).split('.')
            if int(r) <= 9:
                if int(k) <= 9:
                    result.append(f'{r} руб. {k}0 коп.')
                else:
                    result.append(f'{r} руб. {k} коп.')
            else:
                if int(k) <= 9:
                    result.append(f'{r} руб. {k}0 коп.')
                else:
                    result.append(f'{r} руб. {k} коп.')
        elif type(price_list[price_list.index(i)]) == int:
            r = price_list[price_list.index(i)]
            if r <= 9:
                result.append(f'{r} руб. 00 коп.')
            else:
                result.append(f'{r} руб. 00 коп.')
    return ", ".join(result)


def task_b(price_list: list) -> None:
    print(id(price_list))
    price_list.sort()
    print(price_list)
    print(id(price_list))


def task_c(price_list: list) -> list:
    tmp: list = price_list[::-1]
    return tmp


def task_d(price_list: list) -> list:
    return task_c(price_list)[:5]


if __name__ == '__main__':
    prices: list = [57.8, 46.51, 2, 154.3, 2.4, 24, 58.4, 34, 5, 7.2, 14.2, 32.4, 33, 5.19, 8.8, 91.4]

    print('Task a')
    print(task_a(prices))
    print('Task b')
    task_b(prices)
    print('Task c')
    print(task_c(prices))
    print('Task d')
    print(task_d(prices))