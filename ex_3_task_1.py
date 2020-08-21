"""
В диапазоне натуральных чисел от 2 до 99 определить,
сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
"""
a = [i for i in range(2, 100)]
b = [j for j in range(2, 10)]

print("В диапазоне чисел [2..99]: ")
for div in b:
    count = 0
    for numb_to_div in a:
        if numb_to_div % div == 0:
            count += 1

    print(f"количество чисел кратных {div} равно {count}")

