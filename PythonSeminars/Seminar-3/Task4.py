# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

grades = input().split()
grades = list(map(int, grades))
min_grade = min(grades)
max_grade = max(grades)
for i in range(len(grades)):
    if grades[i] == max_grade:
        grades[i] = min_grade
        
print(' '.join(map(str, grades)))