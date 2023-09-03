# Пользователь вводит строку из нескольких слов,
# разделённых пробелами. Вывести каждое слово с
# новой строки. Строки нужно пронумеровать.
# Если слово длинное, выводить только первые 10 букв в слове.

strok = input("Введите строку => ")
count_symbol = 1
count_word = 1
print('1. ', end='')
for i in range(len(strok)):
    if count_symbol <= 10:
        print(strok[i], end='')
    if strok[i] == " ":
        count_symbol = 0
        count_word += 1
        print()
        print(count_word, '. ', end='', sep='')
    count_symbol += 1
