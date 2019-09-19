"""
Черненко Тимофей группа КИ19-16/2Б
База данных с  показателями филиалов
Вариант 25
"""
from random import randint
from datetime import datetime


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
            firm[j][i] = randint(10000, 100000)  # рандомные значения для firm

    print("БАЗА ДАННЫХ ФИРМЫ\n" + "Время:"
          + datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S"))
    print("Выберите действие:\n" + "1:Показать базу данных\n" +
          "2:Посчитать средние значения показателей")
    choose = input("Введите 1 или 2:")

    while choose != '1' and choose != '2':  # Проверка на правильность выбранного действия
        choose = input("Введите 1 или 2:")

    if choose == '1':  # действие 1
        print("ВСЕ ПОКАЗАТЕЛИ ФИРМЫ:\n")
        for j in firm:
            print(str(j) + ":" + str(firm[j]))  # вывод показателей фирмы

        print("")  # отступ

    res = [0]*5
    for j in firm:
        val = list(firm[j].values())
        for i in range(len(val)):
            res[i] += val[i]
    if choose == "2":  # действие 2
        print("CРЕДНИЕ ЗНАЧЕНИЯ ПОКАЗАТЕЛЕЙ ФИРМЫ:\n")
        for i in range(len(res)):  # цикл для вывода средних значений показателей firm
            res[i] /= len(firm)
            print("Cреднее значение '" + list(firm['br1'].keys())[i] +
                  "' показателя по всей фирме:" + str(res[i]))


get_dict()
