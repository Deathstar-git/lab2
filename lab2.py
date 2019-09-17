"""
Черненко Тимофей группа КИ19-16/2Б
База данных с  показателями филиалов
Вариант 25
"""
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
    res = [0]*5
    for j in firm:

        val = list(firm[j].values())
        for i in range(len(val)):
            res[i] += val[i]

    for i in range(len(res)):
        res[i] /= len(firm)
        print("Cреднее значение " + list(firm['br1'].keys())[i] + " показателя по всей фирме:" + str(res[i]))


get_dict()
