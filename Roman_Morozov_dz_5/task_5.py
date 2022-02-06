def get_uniq_numbers(src: list):
    tmp: dict = {}
    for i in src:
        tmp[i] = tmp.get(i, 0) + 1
    result = [j for j in src if tmp[j] == 1]
    return result


src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(*get_uniq_numbers(src))