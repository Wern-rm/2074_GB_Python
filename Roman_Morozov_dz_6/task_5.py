import sys

from task_4 import create_user_hobby

if len(sys.argv) == 1:
    print("Error: Not files.")
    sys.exit()
elif len(sys.argv) > 4:
    print('Error: More than 3 files are specified.')
    sys.exit()
elif len(sys.argv) < 4:
    print('Error: More than 3 files are specified.')
    sys.exit()

create_user_hobby(sys.argv[1], sys.argv[2], sys.argv[3])