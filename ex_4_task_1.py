"""
Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех уроков.

Примечание. Идеальным решением будет:
● выбрать хорошую задачу, которую имеет смысл оценивать,
● написать 3 варианта кода (один у вас уже есть),
● проанализировать 3 варианта и выбрать оптимальный,
● результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
● написать общий вывод: какой из трёх вариантов лучше и почему.
"""
import timeit
import cProfile

# ex_2_task_3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.

# Срез
def my_slice(num):
    return num[::-1]


# Цикл
def my_reverse(num):
    reverse = 0
    num = int(num)
    while num > 0:
        rest = num % 10
        num = num // 10
        reverse = reverse * 10
        reverse = reverse + rest
    return reverse


# Рекурсия
def my_recursion(num):
    if len(num) == 1:
        return num
    else:
        return num[-1] + my_recursion(num[:-1])


num = "19"
# num = "567"
# num = "1234"

# print(my_slice(num))
# print(my_reverse(num))
# print(my_recursion(num))

# num = "19" нужно раскоментить для использования
print(timeit.timeit("my_slice(num)", number=1000, globals=globals()))   #0.0005686999999999984
cProfile.run("my_slice(num)")
        1    0.000    0.000    0.000    0.000 ex_4_task_1.py:17(my_slice)

print(timeit.timeit("my_reverse(num)", number=1000, globals=globals()))  #0.0011395999999999906
cProfile.run("my_reverse(num)")
        1    0.000    0.000    0.000    0.000 ex_4_task_1.py:22(my_reverse)

print(timeit.timeit("my_recursion(num)", number=1000, globals=globals()))  #0.0008507999999999988
cProfile.run("my_recursion(num)")
      2/1    0.000    0.000    0.000    0.000 ex_4_task_1.py:34(my_recursion)
# _____________________
 #num = "567" нужно раскоментить для использования
print(timeit.timeit("my_slice(num)", number=1000, globals=globals()))   #0.0003574999999999967
cProfile.run("my_slice(num)")
        1    0.000    0.000    0.000    0.000 ex_4_task_1.py:17(my_slice)

print(timeit.timeit("my_reverse(num)", number=1000, globals=globals()))  #0.0014349999999999918
cProfile.run("my_reverse(num)")
        1    0.000    0.000    0.000    0.000 ex_4_task_1.py:22(my_reverse)

print(timeit.timeit("my_recursion(num)", number=1000, globals=globals()))  #0.0016511000000000026
cProfile.run("my_recursion(num)")
      3/1    0.000    0.000    0.000    0.000 ex_4_task_1.py:34(my_recursion)
# _____________________
# num = "1234" нужно раскоментить для использования
print(timeit.timeit("my_slice(num)", number=1000, globals=globals()))   #0.0005817000000000044
cProfile.run("my_slice(num)")
        1    0.000    0.000    0.000    0.000 ex_4_task_1.py:17(my_slice)

print(timeit.timeit("my_reverse(num)", number=1000, globals=globals()))  #0.0029695
cProfile.run("my_reverse(num)")
        1    0.000    0.000    0.000    0.000 ex_4_task_1.py:22(my_reverse)

print(timeit.timeit("my_recursion(num)", number=1000, globals=globals()))  #0.0024272000000000044
cProfile.run("my_recursion(num)")
      4/1    0.000    0.000    0.000    0.000 ex_4_task_1.py:34(my_recursion)

# Вывод:
"""
timeit
my_slice() - работает быстрее всего, т.к. не перебирает числа по кругу, не использует видимый цикл;
срез от конца к началу.
my_reverse() и my_recursion() работают по времени примерно одинаково независимо от входного значения. 
Используется перезапись значений. my_reverse() чем больше num, тем больше итераций цикла; my_recursion() чем больше n, тем больше
раз функция вызовет сама себя

cProfile.run
ncalls – это количество совершенных вызовов;
tottime – это все время, потраченное в данной функции;
percall – ссылается на коэффициент tottime, деленный на ncalls;
cumtime – совокупное время, потраченное как в данной функции, так и наследуемых функциях. 
Второй столбец percall – это коэффициент cumtime деленный на примитивные вызовы;
filename:lineno(function) предоставляет соответствующие данные о каждой функции.

нам интересна функция ex_4_task_1.py - (my_slice), my_reverse() и my_recursion() 

cProfile не выявил медленных функции

Общий вывод: 
самый выгодный алгоритм my_slice() 
"""