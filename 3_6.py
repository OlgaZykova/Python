#6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв
# и возвращающую его же, но с прописной первой буквой.
# Например, print(int_func(‘text’)) -> Text.
#Продолжить работу над заданием. В программу должна попадать строка из слов,
# разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
#
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
#Необходимо использовать написанную ранее функцию int_func().

def int_func(text:str):
    if not text.istitle():
        text = text.capitalize()
    return text

t = 'word'
print(f' Результат работы функции для слова {t}: {int_func(t)}')

my_string = 'first Second third'

string_list=my_string.split()
new_list=[]
for word in string_list:
    new_list.append(int_func(word))
new_string = ' '.join(new_list)

print(f' Результат работы программы для строки {my_string}: {new_string}')