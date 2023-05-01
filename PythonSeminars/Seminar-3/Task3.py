# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes 

from math import sqrt

def check(n):
    for i in range(2, int(sqrt(n)+1)):
        if n % i == 0:
            return "NO"
        return "YES"

num = int(input("Введите число: "))
print(check(num))