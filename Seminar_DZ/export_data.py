# Функция записи данных

def push_data(str):
    str = str.split(';')
    with open('Seminar_DZ\\name.csv', 'a') as name:
        for i in range(0, 5):
            name.write(str[i] + ';')
        name.write('\n')

    with open('Seminar_DZ\\car.csv', 'a') as car:
        car.write(str[0] + ';')
        for i in range(5, 7):
            car.write(str[i] + ';')
        car.write('\n')

    with open('Seminar_DZ\\adress.csv', 'a') as adress:
        adress.write(str[0] + ';')
        for i in range(7, 12):
            adress.write(str[i] + ';')
        adress.write('\n')
