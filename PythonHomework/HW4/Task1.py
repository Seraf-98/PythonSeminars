# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

# import random
# A1 =[random.randint(1, 10) for i in range(int(input("Введите размер: ")))]
# A2 =[random.randint(1, 10) for i in range(int(input("Введите размер: ")))]
# print(A1)
# print(A2)

mol = [int(x) for x in input().split()]
n = mol[0]
m = mol[1]

A1 = [int(x) for x in input().split()]
K1 = set(A1)

A2 = [int(x) for x in input().split()]
K2 = set(A2)

lok = K1 & K2
kool = list(lok)
kool.sort()
print(*kool)
# spisok = []  # second sort method
# for el in K1:
#     if el in K2:
#         spisok.append(el)
# print(spisok)



# def sort(X):
#     if len(X) <= 1:
#         return X
#     else:
#         start = X[0]
#     less = [i for i in X[1:] if i <= start]
#     greater = [i for i in X[1:] if i > start]
#     return sort(less)+[start]+sort(greater)

