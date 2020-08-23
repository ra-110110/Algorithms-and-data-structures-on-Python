# 4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.

# Примечания:
# 1. В заданиях 2, 3, 4, 7, 8, 9 пользователь вводит только натуральные числа.

# начало
# рекурсивный алгоритм i от 1 до a / |-2|:   (шестиугольник)
# a = 1
# b = 0
# b = a + a
# a = ( a / |-2|)
# конец

def sum_s():
    a = 1
    b = 0
    print(a)
    for i in range(n):
        b += a
        a /= -2
        print(a)
    return b


n = int(input('Ввведите количество элементов: '))
z = sum_s()
print('Сумма ряда:', z)
print("*" * 50)

# вариант 2

def rec_metod(i, numb, r_count, common_sum):
    """Рекурсия"""
    if i == r_count:
        print(f"Количество элементов - {r_count}, их сумма - {common_sum}")
    elif i < r_count:
        return rec_metod(i + 1, numb / 2 * -1, r_count, common_sum + numb)


try:
    R_COUNT = int(input("Введите количество элементов: "))
    rec_metod(0, 1, R_COUNT, 0)
except ValueError:
    print("Вы ввели строку! Введите число!")