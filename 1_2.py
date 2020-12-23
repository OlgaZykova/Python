#2. Пользователь вводит время в секундах.
#Переведите время в часы, минуты и секунды и
# выведите в формате чч:мм:сс. Используйте форматирование строк.

SEC_IN_MIN = 60
MIN_IN_HOUR = 60

all_secundes =  int(input('Введите целое число - количество секунд: '))
hours = all_secundes // (SEC_IN_MIN * MIN_IN_HOUR)

minutes = (all_secundes - hours * SEC_IN_MIN * MIN_IN_HOUR) // MIN_IN_HOUR

secundes = (all_secundes - hours * SEC_IN_MIN * MIN_IN_HOUR - minutes * SEC_IN_MIN)

#функция добавляет нолик впереди числа меньше 10 и возвращает строковое значение, соответствующее num
def to_str_num(num):
    if num < 10:
        s_num = '0'+ str (num)
    else:
        s_num = str (num)
    return(s_num)

#выводим итоговый результат на экран, используем форматирование строк
print(f' Итоговый результат: {to_str_num(hours)}:{to_str_num(minutes)}:{to_str_num(secundes)}')