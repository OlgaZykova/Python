# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов.
# В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.

class Equipment:
    def __init__(self, name, location: str):
        self.name = name
        self.location = location


class Printer(Equipment):
    def __init__(self, name, location, is_color=False):
        Equipment.__init__(self, name, location)
        self.is_color = is_color


class Scanner(Equipment):
    def __init__(self, name, location, resolution: int):
        Equipment.__init__(self, name, location)
        self.resolution = resolution


class Xerox(Equipment):
    def __init__(self, name, location, paper_format: str):
        Equipment.__init__(self, name, location)
        self.paper_format = paper_format

my_printer = Printer('Принтер №1','1-124',True)
my_scanner = Scanner("Сканнер №1", '2-202', 1024)
my_xerox = Xerox('Ксерокс №1', '2-12','А4')
