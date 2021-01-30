# Реализовать класс «Дата», функция-конструктор которого должна принимать дату
# в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год
# и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

#Данные для проверки внизу вбиты

class Date:
    @classmethod
    def unpack_date(cls, str_date: str):
        return [int(i) for i in str_date.split('-')]

    @staticmethod
    def date_validation(date_list):
        '''
        метод принимает список вида [dd,mm,yy]
        '''
        if date_list[1] not in range(1, 13):
            print('Недопустимое значение месяца')
            return -1
        if date_list[2] < 0:
            print('Недопустимое значение года')
        if date_list[0] not in range(1, 32):
            print('Дата содержит неверное значение дня месяца')
            return -1
        if (date_list[0] > 30 and date_list[1] not in [1, 3, 5, 7, 8, 10, 12]) or (
                date_list[0] > 29 and date_list[1] == 2):
            print('В этом месяце нет такого количества дней!')
            return -1
        if date_list[0] > 28 and date_list[1] == 2 and date_list[2] % 4 != 0:
            print('В феврале невисокосного года не может быть столько дней')
            return -1
        else:
            return 'Корректная дата'

    def __init__(self, str_date: str):
        '''

      Добавим в ините распаковку и проверку корректности даты
        '''
        if Date.date_validation(Date.unpack_date(str_date)) != -1:
            self.list_date = Date.unpack_date(str_date)
            print('Дата корректна')
        else:
            print('Некорретные данные для инициализации объекта класса')

#проверим без создания объекта класса
print(Date.date_validation(Date.unpack_date('29-3-1999')))

#проверим с созданием объекта класса
A = Date('01-22-1987')