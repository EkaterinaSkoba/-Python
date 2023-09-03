# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и dict.
wint = [12, 1, 2]
sprin = [3, 4, 5]
summ = [6, 7, 8]
aut = [9, 10, 11]
mounth = int(input())
seasons = {1: 'winter', 2: 'spring', 3: 'summer', 4: 'autumn'}

for i in range(3):
    if mounth == wint[i]:
        print(seasons.get(1))
    if mounth == sprin[i]:
        print(seasons.get(2))
    if mounth == summ[i]:
        print(seasons.get(3))
    if mounth == aut[i]:
        print(seasons.get(4))

