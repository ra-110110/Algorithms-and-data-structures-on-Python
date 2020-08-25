"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как коллекция, элементы которой — цифры числа.
Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Примечание: Если воспользоваться функциями hex() и/или int() для преобразования систем счисления,
задача решается в несколько строк.
Для прокачки алгоритмического мышления такой вариант не подходит.
Поэтому использование встроенных функций для перевода из одной системы счисления в другую в данной задаче под запретом.
Вспомните начальную школу и попробуйте написать сложение и умножение в столбик.

Задача считается решённой, если в ней использована как минимум одна коллекция из модуля collections.
"""
# проверить число https://calculatori.ru/perevod-chisel.html
from collections import Counter

list_of_dictionary = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
                      10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
num_1 = list(str(input("Введите первое число шестнадцатеричное число:").upper()))
num_2 = list(str(input("Введите второе число шестнадцатеричное число:").upper()))
print(f'вы ввели - {num_1} и {num_2}')


# из hex в dec
def conv(s):
    a = {}
    for count, element in enumerate(s[::-1]):
        a[count] = element
    sorted_by_value = []
    for key, values in list_of_dictionary.items():
        for count, element in a.items():
            if element == values:
                element = key
                a[count] = element
                sorted_by_value = a

    sum_item = 0
    for k, v in sorted_by_value.items():
        item = v * (16 ** k)
        sum_item += item
    return sum_item


sum_num = conv(num_1) + conv(num_2)
mult_num = conv(num_1) * conv(num_2)


# из dec в hex
def maths(val):
    q = val
    result = ""
    while q != 0:
        r = q % 16
        q = q // 16
        result += list_of_dictionary[r]
    result = ''.join(reversed(result))
    return result
result_s = maths(sum_num)
print(f"сумма чисел в десятичной системе равна {sum_num} => 0x{result_s} или {list(str(result_s))}")
result_m = maths(mult_num)
print(f"сумма чисел в десятичной системе равна {mult_num} => 0x{result_m} или {list(str(result_m))}")


abs_test = Counter(result_m)
# print(abs_test)
