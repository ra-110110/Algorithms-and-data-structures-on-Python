"""
Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части: в одной находятся
элементы, которые не меньше медианы, в другой — не больше медианы.

Примечание: задачу можно решить без сортировки исходного массива.
Но если это слишком сложно, используйте метод сортировки, который не рассматривался на уроках
(сортировка слиянием также недопустима).
"""

from random import randint

int_list = []
m = int(input("Введите натуральное число для массива: "))
size = 2 * m + 1
for i in range(size):
    int_list.append(randint(0, 100))
print(int_list)

# 1 вариант
from numpy import median #модуль

print(median(int_list))

# 2 вариант
from statistics import median #модуль

print(median(int_list))


# 3 вариант
def medianN(lst):
    med = sorted(lst)[int((len(lst) - 1) / 2)]  #ищем центральный элемент отсортированного списка
    print(med)


medianN(int_list)


# 4 вариант (без сортировки)
def medianNum(lst):
    while len(lst) != 1: #удаляем максимальный и минимальные элементы пока не останется один средний
        lst.pop(lst.index(max(lst)))
        lst.pop(lst.index(min(lst)))
    print(*lst)


medianNum(int_list)
