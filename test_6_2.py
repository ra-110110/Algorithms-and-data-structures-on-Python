from sys import getsizeof, getrefcount


# 2 вариант
def sum_numbers(num):
    sum_ = 0
    for f in num:
        sum_ += int(f)
    return sum_


list_number = [i for i in input('Введите числа через пробел и нажмите Enter: ').split()]

max_n = 0
max_s = 0
for i in list_number:
    if sum_numbers(i) > max_s:
        max_n = i
        max_s = sum_numbers(i)

print(f'максимальное число {max_n} имеет сумму цифр: {max_s}')

# удалим временные значения
del i


# del list_number ---можно также удалить, но оставим для разбора значения


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
show(max_n)
show(list_number)
print(getsizeof(max_s) + getsizeof(max_n))
print(getsizeof(max_s) + getsizeof(max_n) + getsizeof(list_number) + sum(getsizeof(x) for x in list_number))
"""
Введите числа через пробел и нажмите Enter1 2 25 0
максимальное число 25 имеет сумму цифр: 7
type=<class 'int'>, size=14, count=14 obj=7
type=<class 'str'>, size=27, count=5 obj=25
type=<class 'list'>, size=44, count=4 obj=['1', '2', '25', '0']
type=<class 'str'>, size=26, count=12 obj=1
type=<class 'str'>, size=26, count=6 obj=2
type=<class 'str'>, size=27, count=6 obj=25
type=<class 'str'>, size=26, count=6 obj=0
41
190
"""
del list_number
