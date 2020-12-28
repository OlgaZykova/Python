# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

my_str = input('Введите строку из слов, разделенных пробелами: ')
max_len = 10
my_str = my_str.split()
new_list = []
for i in my_str:
    if len(i) > max_len:
        print(i)
        new_list.append(i[:max_len])
    else:
        new_list.append(i)

#вывод нумерованного списка
for ind, el in enumerate(new_list):
    print(ind+1, el)
