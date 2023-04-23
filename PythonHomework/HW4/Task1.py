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

# size_1 = int(input('Введите количество элементов первого списка: '))
# spisok_1 = []
# for el_1 in range(size_1):
#     spisok_1.append(random.randint(-9, 9))
# print(spisok_1)

# size_2 = int(input('Введите количество элементов второго списка: '))
# spisok_2 = []
# for el_2 in range(size_2):
#     spisok_2.append(random.randint(-9, 9))
# print(spisok_2)

# equal = set()

# for el_1 in range(len(spisok_1)):
#   if spisok_1[el_1] in spisok_2:
#     equal.add(spisok_1[el_1])

# eq_list = list(equal)
# eq_list.sort()
# print(f'Одинаковые элементы в списках: {eq_list}')