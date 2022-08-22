number = int(input('Введите целое положительное число: '))
maxim = 0
while number > 0:
    if number % 10 > maxim:
        maxim = number % 10
    number //= 10
print('Максимальная цифра в введеном числе:', maxim)
