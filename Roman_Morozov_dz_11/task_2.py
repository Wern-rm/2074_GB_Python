class Division:

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    @staticmethod
    def try_division(numerator, denominator):
        try:
            return numerator / denominator
        except ZeroDivisionError:
            return f'Деление на ноль невозможно'
        except TypeError:
            return f'Не является числом'


if __name__ == '__main__':
    div = Division.try_division(100, '5')
    print(div)
    print(Division.try_division(35, 7))
    print(Division.try_division(7, 0))