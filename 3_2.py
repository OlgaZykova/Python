#2. Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def user (name,surname,year,city,email='default@mail.ru',phone_number=111):
    print(f'Данные пользователя: {name}, {surname}, {year}, {city}, {email}, {phone_number}')

a = 'Вася'
b = 'Иванов'
c = '1990'
d = 'Москва'
e = 'qq@mail.ru'
f = '8800'

user(a,b,c,d,e,f)
print('А ниже проверим подстановку значений по умолчанию')
user(a,b,c,d)