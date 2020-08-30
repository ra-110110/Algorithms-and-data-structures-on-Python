from sys import getsizeof, getrefcount

# 3 вариант
list_number = [int(x) for x in input("Введите последовательность натуральных чисел и нажмите Enter: ").split()]
max_num = max(map(int, list_number))


def sum_digits(num):
    return num % 10 + sum_digits(num // 10) if num > 9 else num


print(f'максимальное число {max_num} имеет сумму цифр: {sum_digits(max_num)}')


# удалим временные значения
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


show(list_number)
show(max_num)
print(getsizeof(max_num))
print(getsizeof(max_num) + getsizeof(list_number) + sum(getsizeof(x) for x in list_number))
"""
Введите последовательность натуральных чисел и нажмите Enter: 1 2 25 0
максимальное число 25 имеет сумму цифр: 7
type=<class 'list'>, size=44, count=4 obj=[1, 2, 25, 0]
type=<class 'int'>, size=14, count=93 obj=1
type=<class 'int'>, size=14, count=80 obj=2
type=<class 'int'>, size=14, count=7 obj=25
type=<class 'int'>, size=12, count=190 obj=0
type=<class 'int'>, size=14, count=6 obj=25
14
112
"""
del list_number
