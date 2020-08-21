"""
Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки
и записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.

"""
# вариант 1 без ввода с клавиатуры
"""
from random import randint

n = 5
m = 4

a = [[0 for i in range(m)] for j in range(n)]

for j in range(n):
    row_sum = 0
    for i in range(0, m):
        a[j][i] = randint(0, 10)
        row_sum += a[j][i]
        print(f"{a[j][i]}", end='   ')
    print(f"{row_sum:3}")
"""
# вариант 2 по заданию
n = 5
m = 4
a = []

for j in range(n):
    s = []
    row_sum = 0
    r = j + 1
    print(f"{r}-я строка")
    for i in range(m):
        row = int(input("Введите число: "))
        row_sum += row
        s.append(row)
    s.append(row_sum)
    a.append(s)
for i in a:
    print(*i)
