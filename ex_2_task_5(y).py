# 5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.


def cycle_method(from_symbol, to_symbol, output_str=""):
    """Цикл"""
    for i in range(from_symbol, to_symbol):
        if i <= LAST_ASCII_NUM:
            output_str += f"{i} - {chr(i)}"
    return output_str


first_ASCII_num = 32
LAST_ASCII_NUM = 127
STEP = 10

print("Это вывод цикла: ")
for i in range(first_ASCII_num, LAST_ASCII_NUM + 1, STEP):
    print(cycle_method(i, i + STEP))
