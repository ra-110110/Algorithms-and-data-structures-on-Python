# 6. В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться, больше или меньше введенное пользователем число, чем то, что загадано.
# Если за 10 попыток число не отгадано, вывести правильный ответ.

# начало
# включаем счетчик кол-ва попыток x = 0
# генерируем случайное число от 1 до 100 равное a
# запускаем бесконечный цикл: # (ромб)
# пока кол-во попыток меньше 10 просим ввести число (b) пользовавтеля:
# если b > a  печатаем "Меньше!"
# увеличиваем счетчик попыток на 1 и снова просим ввести число (b) пользовавтеля
# если a > b  печатаем "Больше!"
# увеличиваем счетчик попыток на 1 и снова просим ввести число (b) пользовавтеля
# если a = b  печатаем "Число верное!"
# Вывод числа  a = a
# Конец

import random

x = 0
a = random.randint(1, 100)
while x < 10:
    b = int(input("число: "))
    if b > a:
        print("Меньше!")
    elif b < a:
        print("Больше!")
    elif b == a:
        print("Число верное!")
        break
    x += 1
print("Это число: ", a)
