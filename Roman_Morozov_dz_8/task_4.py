from functools import wraps


def checker(number):
    if not isinstance(number, int) or number < 0:
        raise ValueError(f'wrong val {type(number)}')


def val_checker(validation_func):
    def inside(func):
        @wraps(func)
        def wrapper(num):
            validation_func(num)
            return func(num)
        return wrapper
    return inside


@val_checker(checker)
def calc_cube(x):
    """Возведение числа в третью степень"""
    return x ** 3


if __name__ == '__main__':
    print(calc_cube(5))
    print(calc_cube('ss'))