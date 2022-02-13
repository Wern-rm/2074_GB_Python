import sys
import json


def prepare_dataset(path_users_file: str, path_hobby_file: str) -> dict:
    with open(path_users_file, 'r', encoding='utf-8') as fr:
        user_lines = fr.read().split('\n')

    with open(path_hobby_file, 'r', encoding='utf-8') as frr:
        hobby_lines = frr.read().split('\n')

    dict_user_hobby = dict.fromkeys(user_lines)
    if len(hobby_lines) > len(user_lines):
        sys.exit([1])
    elif len(hobby_lines) <= len(user_lines):
        for i in range(len(hobby_lines)):
            dict_user_hobby[user_lines[i]] = hobby_lines[i].split(',')
    return dict_user_hobby


dict_out = prepare_dataset('users.csv', 'hobby.csv')

with open('task_3_result.json', 'w', encoding='utf-8') as fw:
    json.dump(dict_out, fw, ensure_ascii=False, indent=2)
