"""
Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого
числа должна принимать на вход натуральное и возвращать соответствующее простое число.
Проанализировать скорость и сложность алгоритмов.

Первый — с помощью алгоритма «Решето Эратосфена».
Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков.
Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.

Второй — без использования «Решета Эратосфена».
Примечание. Вспомните классический способ проверки числа на простоту.
"""
import timeit
import cProfile
# Решето Эратосфена . Вариант №1 (алгоритм с урока 2)
# 2   3    4   5    6      7   8      9    10     11        12      13   ...  1000

def isSieve(n):
    sieve = [i for i in range(n)]
    sieve[1] = 0

    for i in range(2, n):
        if sieve[i] != 0:
            j = i + i
            while j < n:
                sieve[j] = 0
                j += i
    res = [i for i in sieve if i != 0]
    return res
# print(isSieve(500))
# Решето Эратосфена . Вариант №2
print('*'*100)

def isPrime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n

# print(isPrime(500))
# проверка на скорость и сложность
# №1
print(timeit.timeit('isSieve(5)', number=1000, globals=globals())) #0.003424499999999997
print(timeit.timeit('isSieve(50)', number=1000, globals=globals())) #0.023883299999999996
print(timeit.timeit('isSieve(100)', number=1000, globals=globals())) #0.0519428
print(timeit.timeit('isSieve(200)', number=1000, globals=globals())) #0.1044092
print(timeit.timeit('isSieve(500)', number=1000, globals=globals())) #0.3123439
#
cProfile.run('isSieve(5)')
        1    0.000    0.000    0.000    0.000 ex_4_task_2.py:18(isSieve)
        1    0.000    0.000    0.000    0.000 ex_4_task_2.py:19(<listcomp>)
        1    0.000    0.000    0.000    0.000 ex_4_task_2.py:28(<listcomp>)
cProfile.run('isSieve(50)')
        1    0.000    0.000    0.000    0.000 ex_4_task_2.py:18(isSieve)
        1    0.000    0.000    0.000    0.000 ex_4_task_2.py:19(<listcomp>)
        1    0.000    0.000    0.000    0.000 ex_4_task_2.py:28(<listcomp>)
cProfile.run('isSieve(100)')
        1    0.000    0.000    0.000    0.000 ex_4_task_2.py:18(isSieve)
        1    0.000    0.000    0.000    0.000 ex_4_task_2.py:19(<listcomp>)
        1    0.000    0.000    0.000    0.000 ex_4_task_2.py:28(<listcomp>)
cProfile.run('isSieve(200)')
        1    0.000    0.000    0.000    0.000 ex_4_task_2.py:18(isSieve)
        1    0.000    0.000    0.000    0.000 ex_4_task_2.py:19(<listcomp>)
        1    0.000    0.000    0.000    0.000 ex_4_task_2.py:28(<listcomp>)
cProfile.run('isSieve(500)')
        1    0.000    0.000    0.000    0.000 ex_4_task_2.py:18(isSieve)
        1    0.000    0.000    0.000    0.000 ex_4_task_2.py:19(<listcomp>)
        1    0.000    0.000    0.000    0.000 ex_4_task_2.py:28(<listcomp>)
# №2
print(timeit.timeit('isPrime(5)', number=1000, globals=globals())) # 0.0006012000000000031
print(timeit.timeit('isPrime(50)', number=1000, globals=globals())) # 0.0002723000000000031
print(timeit.timeit('isPrime(100)', number=1000, globals=globals())) # 0.0002728000000000036
print(timeit.timeit('isPrime(200)', number=1000, globals=globals())) # 0.00027189999999999853
print(timeit.timeit('isPrime(500)', number=1000, globals=globals())) # 0.0002720000000000014
cProfile.run('isPrime(5)')
1    0.000    0.000    0.000    0.000 ex_4_task_2.py:34(isPrime)
cProfile.run('isPrime(50)')
1    0.000    0.000    0.000    0.000 ex_4_task_2.py:34(isPrime)
cProfile.run('isPrime(100)')
1    0.000    0.000    0.000    0.000 ex_4_task_2.py:34(isPrime)
cProfile.run('isPrime(200)')
1    0.000    0.000    0.000    0.000 ex_4_task_2.py:34(isPrime)
cProfile.run('isPrime(500)')
1    0.000    0.000    0.000    0.000 ex_4_task_2.py:34(isPrime)
print('*'*100)
# проверим бОльшие значения:
# 500000000 MemoryError
print(timeit.timeit('isSieve(5000)', number=1000, globals=globals())) #3.9537679000000003
print(timeit.timeit('isSieve(10000)', number=1000, globals=globals()))#7.9656359000000005

print(timeit.timeit('isPrime(5000)', number=1000, globals=globals())) #0.0002830999999989814
print(timeit.timeit('isPrime(10000)', number=1000, globals=globals())) #0.00034310000000026264
cProfile.run('isSieve(5000)')
        1    0.003    0.003    0.004    0.004 ex_4_task_2.py:18(isSieve)
        1    0.000    0.000    0.000    0.000 ex_4_task_2.py:19(<listcomp>)
        1    0.000    0.000    0.000    0.000 ex_4_task_2.py:28(<listcomp>)
cProfile.run('isSieve(10000)')
        1    0.006    0.006    0.007    0.007 ex_4_task_2.py:18(isSieve)
        1    0.001    0.001    0.001    0.001 ex_4_task_2.py:19(<listcomp>)
        1    0.001    0.001    0.001    0.001 ex_4_task_2.py:28(<listcomp>)
cProfile.run('isPrime(5000)')
        1    0.000    0.000    0.000    0.000 ex_4_task_2.py:34(isPrime)
cProfile.run('isPrime(10000)')
        1    0.000    0.000    0.000    0.000 ex_4_task_2.py:34(isPrime)
"""
Вывод:
Решето Эратосфена с ростом входного числа работает менее эфективно, чем проверка на простоту числа.
совокупное время (cumtime) в функции isSieve занимает определенное время от 0,000 до 0.007 секунд, 
потраченное как в данной функции, так и наследуемых функциях, в связи с совершенными итерациями.
согласно проверки на скорость timeit isSieve занимает большее время с ростом входного числа n.

Общий вывод:
Проверка на простоту числа наилучший алгоритм.
"""

