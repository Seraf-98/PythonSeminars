# Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.

def my_power(a, b):
    if b == 0:
        return 1
    else:
        return a*my_power(a, b - 1)
    
a = int(input())
b = int(input())
print(my_power(a, b))

