# Продолжить работу над первым заданием. Разработайте методы, которые отвечают
# за приём оргтехники на склад и передачу в определённое подразделение компании. Для хранения данных
# о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру (например, словарь).

all_equipment ={}

class Equipment:
    '''
    при появлении нового объекта он по умолчанию едет на склад
    функция change_location перевозит его со склада в указанную локацию
    '''

    def __init__(self, name):
        self.name = name
        self.location = 'Склад'

    def __str__(self):
        return f'Мое название {self.name}, мое местонахождение: {self.location}'

    def change_location(self, new_location):
        self.location = new_location
        print(f'{self.name} переехал в {self.location}')

class Printer(Equipment):
    '''
    number - параметр  класса, содержит информацию об общем количестве экземпляров класса
    '''
    number = 0

    def __init__(self, name, is_color=False):
        Equipment.__init__(self, name)
        self.is_color = is_color
        Printer.number += 1
        all_equipment['Printer'] = Printer.number


class Scanner(Equipment):
    number = 0

    def __init__(self, name, resolution: int):
        Equipment.__init__(self, name)
        self.resolution = resolution
        Scanner.number += 1
        all_equipment['Scanner'] = Scanner.number

class Xerox(Equipment):
    number = 0

    def __init__(self, name, resolution: int):
        Equipment.__init__(self, name)
        self.resolution = resolution
        Xerox.number += 1
        all_equipment['Xerox'] = Xerox.number


p1 = Printer('Принтер №1', True)
p2 = Printer('Принтер №2', True)
#проверим текущее местоположение p1
print(p1)
p1.change_location('2-212')
#проверим его переезд
print(p1)
s1 = Scanner("Сканнер №1", 1024)
s2 = Scanner("Сканнер №2", 1024)
s3 = Scanner("Сканнер №3", 1024)

x1 = Xerox('Ксерокс №1', 'А4')
x2 = Xerox('Ксерокс №2', 'А4')

#выведем информацию об общем количестве оргтехники
print(f'Общая информация о количестве оргтехники: {all_equipment.items()}')
