import os


def get_dict_size(path: str):
    dict_sizes = {10 ** i: [0, []] for i in range(2, 10)}
    list_keys = list(dict_sizes.keys())
    if not os.path.exists(path):
        print('Path does not exist!')
        return False
    for root, dirs, files in os.walk(path):
        for file in files:
            size = os.stat(os.path.join(path, file)).st_size
            file_format = file[file.rfind('.') + 1:]
            if size <= list_keys[0]:
                dict_sizes[list_keys[0]][0] += 1
                dict_sizes[list_keys[0]][1].append(file_format)
            if list_keys[-1] <= size:
                dict_sizes[list_keys[-1]][0] += 1
                dict_sizes[list_keys[-1]][1].append(file_format)
            for i in range(1, len(list_keys)):
                if list_keys[i - 1] <= size <= list_keys[i + 1]:
                    dict_sizes[list_keys[i]][0] += 1
                    dict_sizes[list_keys[i]][1].append(file_format)
                    break
        for key in dict_sizes.keys():
            dict_sizes[key] = dict_sizes[key][0], list(set(dict_sizes[key][1]))
    return dict_sizes


if __name__ == '__main__':
    print(get_dict_size('/Users/wern/Documents/GB_Python/Roman_Morozov_dz_7'))