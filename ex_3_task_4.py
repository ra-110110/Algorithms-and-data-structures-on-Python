"""
Определить, какое число в массиве встречается чаще всего
"""
import random
# уменьшим размах массива, чтобы были повторы в массиве из 10 чисел
SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 15
var_mass = [random.randint(MIN_ITEM, MAX_ITEM) for i in range(SIZE)]
print(var_mass)
var_mass_set = set(var_mass) # преобразуем в множество
most_common = None # наиболее часто встречаемое значение
count = 0 # его количество
for i in var_mass_set:
    a_count = var_mass.count(i)
    if a_count > count:
        count = a_count
        most_common = i
print(f"Чаще повторяется число - {most_common}") # определяет последнее повторяющееся число если их много и ровное кол-во

# 2 вариант
print(f"Чаще повторяется число - {max(var_mass, key=var_mass.count)}") # определяет первое повторяющееся число если их много и ровное кол-во
