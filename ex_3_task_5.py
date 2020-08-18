"""
В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию (индекс) в массиве.
"""
import random

SIZE = 5  # размер массива 5
MIN_ITEM = -100
MAX_ITEM = 100
var_mass = [random.randint(MIN_ITEM, MAX_ITEM) for i in range(SIZE)]
print(var_mass)

index_of_min = 0
for i in range(len(var_mass)):
    if var_mass[i] < var_mass[index_of_min]:
        index_of_min = i
if var_mass[index_of_min] < 0:
    index_of_negative = index_of_min
    for i in range(len(var_mass)):
        if var_mass[index_of_negative] < var_mass[i] < 0:
            index_of_negative = i
    print(f"Максимальный отрицательный элемент: {var_mass[index_of_negative]}, индекс: {index_of_negative}")
else:
    print("Нет отрицательных чисел!")
