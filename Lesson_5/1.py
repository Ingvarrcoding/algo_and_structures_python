"""
1. Пользователь вводит данные о количестве предприятий, их наименования и
прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
Программа должна определить среднюю прибыль (за год для всех предприятий) и
вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
"""

from collections import namedtuple

enterprise = namedtuple('Enterprise', 'Name q1 q2 q3 q4')
enterprises = []
ent_count = int(input("Введите кол-во предприятий: "))

for e in range(ent_count):
    name = input('Введите наименование предприятия: ')
    quarters = input('Введите прибыль в каждом квартале через пробел: ')
    quarters_float = [float(x) for x in quarters.split()]
    enterprises.append(enterprise(name, *quarters_float[:4]))

aver_profit = namedtuple('Average_profit', 'Enterprise Value')
aver_profits = []

for ent in enterprises:
    sum_profits = 0
    for i in range(1, 5):
        sum_profits += ent[i]
    aver_profits.append(aver_profit(ent.Name, sum_profits/4))

average = sum(ap.Value for ap in aver_profits) / len(aver_profits)

more_aver = []
less_aver = []

for avr in aver_profits:
    if avr.Value > average:
        more_aver.append(avr.Enterprise)
    elif avr.Value < average:
        less_aver.append(avr.Enterprise)

print()
print('Предприятия с прибылью выше средней: ')
print(', '.join(more_aver))
print('Предприятия с прибылью ниже средней: ')
print(', '.join(less_aver))

'''
Введите кол-во предприятий: 3
Введите наименование предприятия: Гога
Введите прибыль в каждом квартале: 12 10 13 18
Введите наименование предприятия: Ваха
Введите прибыль в каждом квартале: 9 17 23 10
Введите наименование предприятия: Гиви
Введите прибыль в каждом квартале: 11 12 13 14

Предприятия с прибылью выше средней: 
Ваха
Предприятия с прибылью ниже средней: 
Гога, Гиви
'''