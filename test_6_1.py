from sys import getsizeof, getrefcount

# 1 вариант
n = int(input("Введите число с новой строки, по окончании введите 'Ноль' и нажмите Enter\n"))
max_s = 0
max_m = 0
while n != 0:
    m = n
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    if s > max_s:
        max_s = s
        max_m = m
    n = int(input())
print(f'максимальное число {max_m} имеет сумму цифр: {max_s}')
# удалим временные значения
del s, m, n


def show(x):
    print(f'type={type(x)}, size={getsizeof(x)}, count={getrefcount(x)} obj={x}')
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                show(key)
                show(value)
        elif not isinstance(x, str):
            for item in x:
                show(item)


show(max_s)
show(max_m)
print(getsizeof(max_s) + getsizeof(max_m))

"""
Введите число, по окончании введите 'Ноль' 
1
2
25
0
максимальное число 25 имеет сумму цифр: 7
type=<class 'int'>, size=14, count=14 obj=7
type=<class 'int'>, size=14, count=5 obj=25
28
"""
