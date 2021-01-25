# 3. Описание задачи не включаю, слишком объемное
import math


class Cell:
    def __init__(self, n):
        self.nucleus = n

    def __str__(self):
        return f'Я клетка c {self.nucleus} ячейками'

    def __add__(self, other):
        if type(other) != Cell:
            raise Exception('Недопустимый операнд для операции сложения')
        new_cell = Cell(self.nucleus + other.nucleus)
        return new_cell

    def __sub__(self, other):
        if type(other) != Cell:
            raise Exception('Недопустимый операнд для операции вычитания')
        if self.nucleus < other.nucleus:
            raise Exception('Количество ячеек у первого операнда меньше, вычитание невозможно')
        else:
            new_cell = Cell(self.nucleus - other.nucleus)
        return new_cell

    def __mul__(self, other):
        if type(other) != Cell:
            raise Exception('Недопустимый операнд для операции умножения')
        new_cell = Cell(self.nucleus * other.nucleus)
        return new_cell

    def __truediv__(self, other):
        if type(other) != Cell:
            raise Exception('Недопустимый операнд для операции деления')
        if other.nucleus == 0:
            raise Exception('Недопустимое количество клеток у второго операнда')
        new_cell = Cell(round(self.nucleus / other.nucleus))
        return new_cell

    def make_order(self, n):
        x = self.nucleus // n
        y = self.nucleus % n
        s = ''
        for i in range(0, x):
            s += '*' * n + '\n'
        s += y * '*'
        return s


my_cell1 = Cell(5)
my_cell2 = Cell(14)
print(my_cell1 + my_cell2)
print(my_cell2 - my_cell1)
# для проверки генерации исключения в случае когда число ячеек первого операнда меньше чем у второго
# print(my_cell1 - my_cell2)
print(my_cell2 * my_cell1)
print(my_cell2 / my_cell1)
#для генерации ошибки это раскомментить
#print(my_cell2 / 2)
print(f'А это результат работы функции my_order для значений {my_cell2.nucleus} и {4}:\n{my_cell2.make_order(4)}')