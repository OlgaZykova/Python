# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции
# сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
class Matrix:
    def __init__(self, s_list):
        '''
        n и m - размерность матрицы
        '''
        self.string = s_list
        self.n = len(self.string)
        self.m = len(self.string[0])

    def print_dimension(self):
        '''
        функция печатает рамерность матрицы
        '''
        print(f'Размерность матрицы = {self.n} * {self.m}')

    def __str__(self):
        str_st = ''
        for st in self.string:
            for el in st:
                str_st += str(el) + ' '
            str_st += '\n'
        return str_st

    def __add__(self, other):
        res = []
        #если размерности матриц не равны, сгенерируем исключение
        if self.n != other.n or self.m != other.m:
            raise Exception("Недопустимая размерность матрицы, невозможно выполнить сложение!")
        else:
            for i in range(0, self.n):
                s = [x + y for x, y in zip(self.string[i], other.string[i])]
                res.append(s)
            return Matrix(res)


m_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

m_list2 = [[1, 2, 3], [4, 5, 6], [2, 3, 4]]
a = Matrix(m_list)
a.print_dimension()
#проверим перегрузку метода __str__
print(f'Матрица, полученная из списка {m_list}:\n{a}')
b = Matrix(m_list2)
#проверим перегрузку метода __add__

print(f'Сумма матриц, полученных из списков {m_list} и {m_list2}:\n{a + b}')
