class EquipmentWarehouse:
    num = 0
    dict_equipment = {'Сканеры': [], 'Принтеры': [], 'Ксероксы': []}

    @classmethod
    def count(cls):
        cls.num += 1

    def full_inventory(self):
        if isinstance(self, Scanner):
            EquipmentWarehouse.dict_equipment['Сканеры'].append(
                (self.name, self.price, self.model_name, self.number_equip, self.work))
        elif isinstance(self, Printer):
            EquipmentWarehouse.dict_equipment['Принтеры'].append(
                (self.name, self.price, self.model_name, self.number_equip, self.work,))
        elif isinstance(self, Xerox): EquipmentWarehouse.dict_equipment['Ксероксы'].append(
            (self.name, self.price, self.model_name, self.number_equip, self.work))

    def __init__(self, name, price, model_name, number_equip, work=True):
        """
        Конструктор класса:
        :param name: название модели оборудования
        :param model_name: модель оборудования
        :param price: цена оборудования
        :param work: работает/не работает, по дефолту работает
        :param number_equip: количество данного оборудования на складе
        """
        self.name = name
        self.model_name = model_name
        self.price = price
        self.number_equip = number_equip
        self.work = work
        self.count()
        self.full_inventory()

    @staticmethod
    def store_info():
        return f'Сканеров {Scanner.num}, принтеров {Printer.num}, ксероксов {Xerox.num}'


class Printer(EquipmentWarehouse):
    num = 0

    def __init__(self, name, price, number_lists, number_equip, type_print, work=True, two_side_print=False):
        """
        Конструктор класса принтера:
        :param two_side_print: двухсторонняя печать
        :param type_print: способу печати: матричный/струйный/лазерный/термо
        """
        super().__init__(name, price, number_lists, number_equip, work)
        self.type_print = type_print
        self.two_side_print = two_side_print


class Scanner(EquipmentWarehouse):
    num = 0

    def __init__(self, name, price, number_lists, number_equip, resolution, work=True, usb_save=False):
        """
        Конструктор класса сканера:
        :param resolution: разрешающая способность сканера
        :param usb_save: Сохранение сразу на USB
        """
        super().__init__(name, price, number_lists, number_equip, work)
        self.resolution = resolution
        self.usb_save = usb_save


class Xerox(EquipmentWarehouse):
    num = 0

    def __init__(self, name, price, number_lists, number_equip, color, work=True, ):
        """
        Конструктор класса ксерокса:
        :param color: Цветная копия
        """
        super().__init__(name, price, number_lists, number_equip, work)
        self.color = color


if __name__ == '__main__':
    p1 = Printer('Hp laser jet', '1544', 100, 5, 'matrix')
    s1 = Scanner('Samsung', 'Mt224', 200, 10, '1200*1200')
    x1 = Xerox('Xerox', '6533', 200, 10, color=True)
    print(EquipmentWarehouse.store_info())
    print(EquipmentWarehouse.dict_equipment)