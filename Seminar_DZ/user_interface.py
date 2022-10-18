# Пользовательский интерфейс

from import_data import get_data
from export_data import push_data

def add_info():
    result_list = get_data()
    id = int(len(result_list))
    string = ''
    string += str(id)+';'
    string += input('Введите фамилию: ') + ';'
    string += input('Введите имя: ') + ';'
    string += input('Введите должность: ') + ';'
    string += input('Введите номер телефона: ') + ';'
    string += input('Введите номер автомобиля: ') + ';'
    string += input('Введите номер парковочного места: ') + ';'
    string += input('Введите город: ') + ';'
    string += input('Введите улицу: ') + ';'
    string += input('Введите дом: ') + ';'
    string += input('Введите номер квартиры: ') + ';'
    string += input('Введите примечание: ') + ';'
    print('Добавляем сотрудника: ', string)
    push_data(string)
