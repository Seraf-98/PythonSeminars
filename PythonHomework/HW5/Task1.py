# Задача 26: Посчитать факториал (произведение 1 до N) 
# и треугольное число (сумма чисел от 1 до N) 
# для числа N ЧЕРЕЗ РЕКУРСИЮ и без циклов

def fac(n):
    if n == 1:
        return 1
    return fac(n - 1) * n

def trnglNum(n):
    if n == 1:
        return 1
    return trnglNum(n - 1) + n

Num = int(input("Введите число: "))
 
print("Факториал =", fac(Num))
print("Треугольное число =", trnglNum(Num))