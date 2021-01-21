# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income). Проверить работу примера
# на реальных данных (создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров).


class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}

    def print(self):
        print(
            f'Имя сотрудника: {self.name} \nФамилия сотрудника: {self.surname}\nДолжность: {self.position}\nДоход: {self._income}')


class Position(Worker):

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


# проверим создание объекта класса Worker
w = Worker('Иван', 'Сидоров', 'медбрат', 30000, 5000)
w.print()
# создадим объект класса Position
a = Position('Александр', 'Иванов', 'врач', 100000, 20000)

# проверим работу методов
print(f'Результат работы метода get_full_name:\n{a.get_full_name()}')
print(f'Результат работы метода get_total_income:\n{a.get_total_income()}')
