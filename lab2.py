"""
Черненко Тимофей группа КИ19-16/2Б
База данных с  показателями филиалов
Вариант 25
"""
# import numpy
from random import randint


def get_dict():
    firm = {'br1': {'revenue': (), 'costs': (), 'debt': (), 'stocks': (), 'donations': ()},
            'br2': {'revenue': (), 'costs': (), 'debt': (), 'stocks': (), 'donations': ()},
            'br3': {'revenue': (), 'costs': (), 'debt': (), 'stocks': (), 'donations': ()},
            'br4': {'revenue': (), 'costs': (), 'debt': (), 'stocks': (), 'donations': ()},
            'br5': {'revenue': (), 'costs': (), 'debt': (), 'stocks': (), 'donations': ()},
            'br6': {'revenue': (), 'costs': (), 'debt': (), 'stocks': (), 'donations': ()},
            'br7': {'revenue': (), 'costs': (), 'debt': (), 'stocks': (), 'donations': ()},
            'br8': {'revenue': (), 'costs': (), 'debt': (), 'stocks': (), 'donations': ()},
            'br9': {'revenue': (), 'costs': (), 'debt': (), 'stocks': (), 'donations': ()},
            'br10': {'revenue': (), 'costs': (), 'debt': (), 'stocks': (), 'donations': ()}, }
    for j in firm:
        for i in firm[j]:
            firm[j][i] = randint(10000, 100000)

    print(firm)
    for i in firm:
        summ = firm[i]['revenue']
        print(summ)


get_dict()

print("GIT is flex")
