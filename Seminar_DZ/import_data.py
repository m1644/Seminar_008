# Функция извлечения данных

from calendar import c
from itertools import zip_longest
from unittest import result
from turtle import width


def summa(a):
    result = ''
    for i in range(3):
        result += a[i]
    return result.replace('\n', '') + '\n'

def get_data():
    with open('Seminar_DZ\\name.csv', 'r') as name:
        name = name.readlines()

    with open('Seminar_DZ\\car.csv', 'r') as car:
        car = car.readlines()

    with open('Seminar_DZ\\adress.csv', 'r') as adress:
        adress = adress.readlines()

    list = [summa(i) for i in zip(name, car, adress)]
    return list
