""""
Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
Требуется вернуть количество различных подстрок в этой строке.
Примечание: в сумму не включаем пустую строку и строку целиком.
Пример работы функции:

func("papa")
6
func("sova")
9
"""
import hashlib


def s_subs(sub):
    result = set()
    for i in range(1, len(sub)):
        for j in range(len(sub)-i+1):
            # result.add(sub[j:i+j])
            result.add(hashlib.sha1(sub[j:i+j].encode('utf-8')).hexdigest())
    return len(result)


string = input('Введите строку: ')
s_subs(string)
print(f'Количество различных подстрок с использованием хеш-функции для строки "{string}" равно {s_subs(string)}')
