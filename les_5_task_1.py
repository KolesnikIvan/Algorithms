"""Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа)
для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий)
и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего."""
from collections import namedtuple
from collections import defaultdict

Enterprise = namedtuple('Enterprise', 'name, quart_1st, quart_2nd, quart_3rd, quart_4th, tot', defaults=('No name', 0, 0, 0, 0, 0))
ent_num = int(input('Введите количество предприятий '))
entrps = []
avg = 0
for i in range(ent_num):
    ent = Enterprise(name=str(input(f'Введите название {i+1}-го предприятия ')), \
                     quart_1st=float(input(f'Введите прибыль {i+1}-го предприятия в 1-м квартале ')), \
                     quart_2nd=float(input(f'Введите прибыль {i+1}-го предприятия в 2-м квартале ')), \
                     quart_3rd=float(input(f'Введите прибыль {i+1}-го предприятия в 3-м квартале ')), \
                     quart_4th=float(input(f'Введите прибыль {i+1}-го предприятия в 4-м квартале ')), \
                    )
    ent = ent._replace(tot=ent.quart_1st + ent.quart_2nd + ent.quart_3rd + ent.quart_4th)
    avg += ent.tot  # ent.quart_1st + ent.quart_2nd + ent.quart_3rd + ent.quart_4th
    entrps.append(ent)
avg /= ent_num

propfitability = defaultdict(list, profitable=[], unprofitable=[])
for ent in entrps:
    if ent.tot > avg:
        propfitability['profitable'].append(ent.name)
    elif ent.tot < avg:
        propfitability['unprofitable'].append(ent.name)
print(propfitability)
