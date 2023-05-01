# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных

import random

Num = int(input("Введите размер массива: "))
Array =[random.randint(1, 3) for i in range(Num)]

print(Array)
Array.sort()
print(Array)

count = 0

for i in range(0, len(Array)-1):
    for j in range(i+1, len(Array)):
        if Array[i] == Array[j]:
            count+=1

print(count)