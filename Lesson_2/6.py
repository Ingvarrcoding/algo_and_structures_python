"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
"""

'''
from random import random
n = round(random() * 100)
i = 1
print("Компьютер загадал число. Отгадайте его. У вас 10 попыток")
while i <= 10:
    u = int(input(str(i) + '-я попытка: '))
    if u > n:
        print('Много')
    elif u < n:
        print('Мало')
    else:
        print('Вы угадали с %d-й попытки' % i)
        break
    i += 1
else:
    print('Вы исчерпали 10 попыток. Было загадано', n)
'''

import random
def trying(count, number):
    inp = int(input(f"Попытка №{count}: "))
    if count == 10 or inp == number:
        if inp == number:
            print("Верно!")
        print(f"Загаданное число: {number}")
    else:
        if inp > number:
            print(f"Загаданное число меньше, чем {inp}")
        else:
            print(f"Загаданное число больше, чем {inp}")
        trying(count + 1, number)
trying(1, random.randint(0, 100))

