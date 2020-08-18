"""
В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.
"""
import random

SIZE = 10  # размер массива 10
MIN_ITEM = -100
MAX_ITEM = 100
var_mass = [random.randint(MIN_ITEM, MAX_ITEM) for i in range(SIZE)]
print(var_mass)

index_of_min1 = 0
index_of_min2 = 0

for i in range(0, len(var_mass)):
    if var_mass[i] < var_mass[index_of_min1]:
        index_of_min1 = i
        a = index_of_min1
        if var_mass[a] < var_mass[index_of_min2]:
            index_of_min1 = a
    elif var_mass[i] < var_mass[index_of_min2]:
        index_of_min2 = i

print(f"Минимальный элемент №1 - {var_mass[index_of_min1]}")
print(f"Минимальный элемент №2 - {var_mass[index_of_min2]}")

