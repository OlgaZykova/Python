# Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число». Реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта. Для этого создаёте экземпляры класса (комплексные числа),
# выполните сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.
class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f'{self.a}+{self.b}i'

    def __add__(self, other):
        return Complex(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return Complex(self.a*other.a - self.b*other.b, self.b*other.a + self.a*other.b)


x = Complex(2, 3)
y = Complex(3, 4)
print(x)
print(y)
print(f'Сумма: {x+y}')
print(f'Умножение: {x*y}')