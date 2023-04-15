x = int(input("Введите сумму чисел: "))
y = int(input("Введите произведение чисел: "))
for i in range(x):
    for j in range(y):
        if x == i + j and y == i * j:
            print(i, j)