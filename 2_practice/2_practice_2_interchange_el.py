N = int(input('Введите количество эл-ов массива: '))
my_list = [0]*N
print("Введите элементы массива:")
for i in range(N):
    my_list[i] = int(input())
print(my_list)
i = 1
while i < N:
    my_list[i-1], my_list[i] = my_list[i], my_list[i-1]
    i += 2
print(my_list)
