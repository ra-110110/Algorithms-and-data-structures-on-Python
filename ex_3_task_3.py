"""
В массиве случайных целых чисел поменять
местами минимальный и максимальный элементы.
"""
import random

SIZE = 5  # размер массива 5
MIN_ITEM = 0
MAX_ITEM = 10000
var_mass = [random.randint(MIN_ITEM, MAX_ITEM) for i in range(SIZE)]
print(var_mass)
# print(var_mass[:5])  # размер массива 5 цифр
# max_el = var_mass.index(max(var_mass))
# min_el = var_mass.index(min(var_mass))
index_of_min = 0
index_of_max = 0
for i in range(0, len(var_mass)):
    if var_mass[i] > var_mass[index_of_max]:
        index_of_max = i
    if var_mass[i] < var_mass[index_of_min]:
        index_of_min = i
var_mass[index_of_min], var_mass[index_of_max] = var_mass[index_of_max], var_mass[index_of_min]
print(var_mass)
# var_m_new = []
# var_m_new.append(var_mass)
# print(*var_m_new)
