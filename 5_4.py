# #4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение
# и считывающую построчно данные. При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

my_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open('4.txt', 'r') as f_1:
    data = f_1.readlines()
new_data = []
for line in data:
    str_line = line.split()
    new_data.append([my_dict[str_line[0]] + ' ' + str_line[2]])

with open('new_4.txt', 'w', encoding='utf-8') as f_2:
    for line in new_data:
        print(f'{line[0]}', file=f_2)
