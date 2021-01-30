# Продолжить работу над вторым заданием. Реализуйте механизм валидации
# вводимых пользователем данных. Например, для указания количества принтеров, отправленных
# на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.

#Логика реализации классов отличается от реализованной в 8_5

class Store:
    '''
    содержит информацию о состоянии склада
    словарь store_content содержит id элементов оборудования по категориям
    init создает пустой склад
    '''

    def __init__(self):
        self.store_content = {'Printers': [], 'Scanners': [], 'Xeroxes': []}
    '''
    update_store кладет в склад технику опр типа с переданными id
    по факту передаваться всегда будет только один ид, не осилила реализацию нескольких
    да и в логику реализации классов не лезло
    '''
    def update_store(self, eq_type, *ids):
        for i in ids:
            self.store_content[eq_type].append(i)

    '''
    проверка передаваемых id
    '''
    @staticmethod
    def id_validation(id):
        if type(id) != int:
            raise ValueError
    '''
    удаляет объкты с переданным id со склада
    '''
    def remove_from_store(self, id):
        try:
            self.id_validation(id)
        except ValueError:
            print('Неверно передан id')
        else:
            for i in self.store_content.items():
                if id in i[1]:
                    k = i[0]
            self.store_content[k].remove(id)


class Equipment:
    '''
    при появлении нового объекта он по умолчанию едет на склад
    контректный склад будет прописан в атрибуты экземляра оргтехники при его создании
    id - имеет уникальное значение для каждого экземпляра
    '''
    id = 0

    def __init__(self, name, st: Store, eq_type=None):
        self.name = name
        self.st = st
        self.location = 'Склад'
        Equipment.id += 1

    def __str__(self):
        return f' Мой id = {self.id}, мое название {self.name}, мое местонахождение: {self.location}'
    '''
    change_location меняет локацию объекта на новую,
    так же обрабатываются случаи перемещения со склада и на склад
    с изменением состояния склада
    '''
    def change_location(self, new_location):
        if self.location == new_location:
            print('Новая локация совпадает с исходной')
        elif self.location == 'Склад':
            self.st.remove_from_store(self.id)
        elif new_location == 'Склад':
            self.st.update_store(self.eq_type, self.id)
        self.location = new_location
        print(f'{self.name} переехал в {self.location}')


class Printer(Equipment):
    '''
    при создании объекта класса помещаем его на склад и обновляем информацию о складе
    '''
    def __init__(self, name, st: Store, is_color=False):
        Equipment.__init__(self, name, st)
        self.is_color = is_color
        self.eq_type = 'Printers'
        self.id = Equipment.id
        self.st.update_store('Printers', self.id)


class Scanner(Equipment):

    def __init__(self, name, st, resolution: int):
        Equipment.__init__(self, name, st)
        self.resolution = resolution
        self.id = Equipment.id
        self.eq_type = 'Scanners'
        self.st.update_store('Scanners', self.id)


class Xerox(Equipment):
    def __init__(self, name, st, resolution: int):
        Equipment.__init__(self, name, st)
        self.resolution = resolution
        self.id = Equipment.id
        self.eq_type = 'Xeroxes'
        self.st.update_store('Xeroxes', self.id)


# создаем склад, на который будем класть все создаваемые принтеры
equipment_store = Store()
# проверим, что склад пуст
print(equipment_store.store_content)

# насоздаем оргтехники в склад
p1 = Printer('Принтер №1', equipment_store, True)
p2 = Printer('Принтер №2', equipment_store)

s1 = Scanner("Сканнер №1", equipment_store, 1024)
s2 = Scanner("Сканнер №2", equipment_store, 1024)
s3 = Scanner("Сканнер №3", equipment_store, 1024)

x1 = Xerox('Ксерокс №1', equipment_store, 'А4')
print(x1)
x2 = Xerox('Ксерокс №2', equipment_store, 'А4')

print(f'Содержимое склада после заполнения: {equipment_store.store_content.items()}')
s2.change_location('2-12')
print(f'Содержимое склада после переезда одного сканнера: {equipment_store.store_content.items()}')
s2.change_location('Склад')
print(f'Содержимое склада после возвращения сканнера {equipment_store.store_content.items()}')
# проверка корректности валидации

equipment_store.remove_from_store('txt')
x2.change_location('3-13')
print(f'Содержимое склада после переезда одного ксерокса: {equipment_store.store_content.items()}')
print(equipment_store.store_content.items())
