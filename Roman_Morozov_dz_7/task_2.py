import os


def create(structure: str):
    path_dir = os.getcwd()
    with open(structure, 'r', encoding='utf-8') as fr:
        parent_name = fr.readline().replace('\n', '')
        while parent_name:
            if not parent_name.startswith('    '):
                os.mkdir(os.path.join(path_dir, parent_name))
                os.chdir(os.path.join(path_dir, parent_name))
                first_dir = (os.getcwd())
                parent_name = fr.readline().replace('\n', '')
                i = 1
            else:
                while True:
                    if parent_name.startswith('    ' * i) and not (os.path.exists(parent_name.strip('    ' * i))):
                        if parent_name.endswith('.py') or parent_name.endswith('.html'):
                            with open(parent_name.strip('    ' * i), 'w', encoding='utf-8') as fw:
                                pass
                        elif not (parent_name.endswith('.py') or parent_name.endswith('.html')):
                            child_dir_name = parent_name.strip('    ' * i)
                            os.mkdir(os.path.join(child_dir_name))
                        parent_name = fr.readline().replace('\n', '')
                        if parent_name.startswith('    ' * (i + 1)):
                            i += 1
                            os.chdir(os.path.join(child_dir_name))
                        elif not parent_name.startswith('    '):
                            break
                    elif os.path.exists(os.path.join(path_dir, first_dir, parent_name.strip('    '))):
                        parent_name = fr.readline().replace('\n', '')
                        break
                    elif parent_name.startswith('    ') and not parent_name.startswith('    ' * 2):
                        os.mkdir(os.path.join(path_dir, first_dir, parent_name.strip('    ')))
                        os.chdir(os.path.join(path_dir, first_dir, parent_name.strip('    ')))
                        i = 2
                        break


if __name__ == '__main__':
    create('config.yaml')