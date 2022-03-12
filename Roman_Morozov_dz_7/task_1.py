import os


def create_project_structure() -> None:
    project_name = 'my_project'
    project_dirs = ['settings', 'mainapp', 'adminapp', 'authapp']
    path = os.path.join(os.getcwd(), project_name)
    if not os.path.exists(path):
        os.mkdir(path)
    os.chdir(path)
    for i in project_dirs:
        i_path = os.path.join(i)
        if not os.path.exists(i_path):
            os.mkdir(i_path)


if __name__ == '__main__':
    create_project_structure()