# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.


class ZeroDivision(Exception):
    def __init__(self,txt='Ваш делитель равен 0'):
        self.txt = txt

dividend = int(input('Введите делимое: '))
divider = int(input('Введите делитель: '))
try:
    if divider == 0:
        raise ZeroDivision('Вы ввели ноль в качестве делителя')
except ZeroDivision as e:
    print(e)
else:
    print(f'Результат деления: {dividend/divider}')


