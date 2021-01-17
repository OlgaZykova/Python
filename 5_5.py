#5. Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open('5.txt','r') as f:
    data = f.readlines()
for line in data:
    str_line = line.split()
    numbers = [int(i) for i in str_line]
    print(f'Сумма чисел из файла: {sum(numbers)}')