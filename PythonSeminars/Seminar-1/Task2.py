# В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для них новыми партами.
# За каждой партой может сидеть два учащихся. Известно количество учащихся в каждом из трех классов.
# Выведите наименьшее число парт, которое нужно приобрести для них.
# **Input:**
# 20
# 21
# 22
# **Output:**
# 32

class1 = int(input("Количество человек в классе №1: "))
print(type(class1))
class2 = int(input("Количество человек в классе №2: "))
print(type(class2))
class3 = int(input("Количество человек в классе №3: "))
print(type(class3))
x = round((class1 + class2 + class3)/2)
print(x)
print(type(x))