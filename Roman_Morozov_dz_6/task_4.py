import sys


def create_user_hobby(path_users_file: str, path_hobby_file: str, result_file: str):
    with open(path_users_file, 'r', encoding='utf-8') as fr:
        user_lines = fr.read().split('\n')

    with open(path_hobby_file, 'r', encoding='utf-8') as frr:
        hobby_lines = frr.read().split('\n')

    if len(hobby_lines) > len(user_lines):
        sys.exit([1])

    data = []
    for i in range(len(user_lines)):
        if i < len(hobby_lines):
            d = f"{user_lines[i]}: {hobby_lines[i]}"
            data.append(d)
        else:
            d = f"{user_lines[i]}: {None}"
            data.append(d)

    with open(result_file, 'w') as f:
        print("\n".join(map(str, data)), file=f)


create_user_hobby('users.csv', 'hobby.csv', 'users_hobby.txt')