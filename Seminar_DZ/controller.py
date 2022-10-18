# Запуск пользовательского интерфейса

from import_data import get_data
from user_interface import add_info

def operations():
    print('Выберите действие: \n\
        1 - вывести информацию о сотрудниках \n\
        2 - добавить запись \n\
        3 - выход из программы')
    a = input('Введите номер операции: ')

    while True:
        if a == '1':
            print(*get_data())
            operations()
        if a == '2':
            add_info()
            operations()
        if a == '3':
            exit()
