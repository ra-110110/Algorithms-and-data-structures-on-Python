"""
Задача считается решённой, если в ней использована как минимум одна коллекция из модуля collections.

Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа)
для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий)
и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
"""

from collections import namedtuple


def calc():
    ent = int(input('Введите количество предприятий: '))

    Companies = namedtuple('Company', 'name, profit_1, profit_2, profit_3, profit_4')
    profit_ent = {}

    for i in range(ent):
        company = Companies(
            name=input(str(i + 1) + '-е предприятие: '),
            profit_1=float(input('Прибыль за 1-й квартал: ')),
            profit_2=float(input('Прибыль за 2-й квартал: ')),
            profit_3=float(input('Прибыль за 3-й квартал: ')),
            profit_4=float(input('Прибыль за 4-й квартал: '))
        )

        profit_ent[company.name] = round(
            ((company.profit_1 + company.profit_2 + company.profit_3 + company.profit_4) / ent), 2)
        print(f'Средняя прибыль предприятия - {profit_ent} ден.ед.')

    mean = 0
    for value in profit_ent.values():
        mean += value
        mean = mean / ent

    for key, value in profit_ent.items():
        if value > mean:
            print(f"{key} - прибыль выше среднего")
        elif value < mean:
            print(f"{key} - прибыль ниже среднего")
        elif value == mean:
            print(f"{key} - Среднее значение прибыли")


calc()
