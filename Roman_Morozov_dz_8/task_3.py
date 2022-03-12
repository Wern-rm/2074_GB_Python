from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(*args):
        for i in range(len(args)):
            if i < len(args) - 1:
                print(f'{wrapper.__name__}({args[i]}: {type(args[i])}), ', end='')
            elif i == len(args) - 1:
                print(f'{wrapper.__name__}({args[i]}: {type(args[i])})')
    return wrapper


@type_logger
def calc_cube(x):
    print(x ** 3)


if __name__ == '__main__':
    calc_cube(3, 5, 10, 17, 129, 3.3)
