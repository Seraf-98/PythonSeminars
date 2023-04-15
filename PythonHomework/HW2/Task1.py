x = int(input("Введите количество монет: "))
count0 = 0
count1 = 0
for value in range(x):
    y = int(input())
    if y == 0:
        count0 += 1
    else: count1 += 1
if count0 < count1:
    print(f"Количество орлов которые нужно перевернуть = {count0}")
else: print(f"Количество решек которые нужно перевернуть = {count1}")
