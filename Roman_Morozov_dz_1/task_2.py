__author__ = 'Roman Morozov'


def sum_list_1(dataset: list) -> int:
    result_sum: int = 0
    for i in dataset:
        s: int = 0
        current_value: int = i
        while i != 0:
            s = s + i % 10
            i = i // 10
        if s % 7 == 0:
            result_sum += current_value
    return result_sum


def sum_list_2(dataset: list) -> int:
    for i in range(len(dataset)):
        dataset[i] += 17
    return sum_list_1(dataset)


def sum_list_3(dataset: list) -> int:
    result_sum: int = 0
    for i in dataset:
        i += 17
        s: int = 0
        current_value: int = i
        while i != 0:
            s = s + i % 10
            i = i // 10
        if s % 7 == 0:
            result_sum += current_value
    return result_sum


if __name__ == '__main__':
    print(sum_list_1([x ** 3 for x in range(1, 1000, 2)]))
    print(sum_list_2([x ** 3 for x in range(1, 1000, 2)]))
    print(sum_list_3([x ** 3 for x in range(1, 1000, 2)]))
