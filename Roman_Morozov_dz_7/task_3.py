import os
import shutil


def move_templates(start_path: str):
    os.chdir(start_path)
    paths_templates = []
    for root, dirs, files in os.walk(start_path):
        if 'templates' in dirs:
            paths_templates.append(os.path.join(root, 'templates'))
    os.mkdir('templates')
    for path in paths_templates:
        shutil.copytree(path, 'templates', dirs_exist_ok=True)


if __name__ == '__main__':
    move_templates(os.path.join(os.getcwd(), 'my_project'))