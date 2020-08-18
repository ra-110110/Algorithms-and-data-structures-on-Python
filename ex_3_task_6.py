"""
В одномерном массиве найти сумму элементов,
находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""
import random
import copy

SIZE = 10  # размер массива 10
MIN_ITEM = 0
MAX_ITEM = 100
var_mass = [random.randint(MIN_ITEM, MAX_ITEM) for i in range(SIZE)]
print(var_mass)

index_of_min = 0
index_of_max = 0
for i in range(0, len(var_mass)):
    if var_mass[i] > var_mass[index_of_max]:
        index_of_max = i
    if var_mass[i] < var_mass[index_of_min]:
        index_of_min = i
print(f"Минимальный элемент - {var_mass[index_of_min]}")
print(f"Максимальный элемент - {var_mass[index_of_max]}")

if index_of_max > index_of_min:
    print(f"Ряд: {var_mass[index_of_min+1:index_of_max]}")
    new_arr = copy.copy(var_mass[index_of_min+1:index_of_max])
else:
    print(f"Ряд: {var_mass[index_of_max+1:index_of_min]}")
    new_arr = copy.copy(var_mass[index_of_max+1:index_of_min])

s = 0
for i in range(0, len(new_arr)):
    s += new_arr[i]
print(f"Сумма ряда: {s}")
