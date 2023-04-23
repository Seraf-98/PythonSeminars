# Задача 24

n = int(input())
arr = list()
for i in range(n):
    x = int(input())
    arr.append(x)

    
arr_count = list()
for i in range(len(arr)-1):
    arr_count.append(arr[i-2] + arr[i-1] + arr[i])
# arr_count.append(arr[-2] + arr[-1] + arr[0])
print(max(arr_count))



# bush = int(input('Введите количество кустов: '))
# garden = []
# for i in range(bush):
#     garden.append(random.randint(0, 30))
# print(garden)

# max = 0

# for i in range(-2, bush-2):
#   summa = garden[i]
#   summa += garden[i+1] + garden[i+2]
#   if summa > max:
#     max = summa
#   i += 1
  
# print(f'Максимальное количество ягод - {max}')