"""
1. Подсчитать, сколько было выделено памяти под переменные в ранее
разработанных программах в рамках первых трех уроков. Проанализировать
результат и определить программы с наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Результаты анализа вставьте в виде
комментариев к коду. Также укажите в комментариях версию Python
и разрядность вашей ОС.
"""

'''
Задача №3 из ДЗ_2.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.
'''

from memory_profiler import profile

n = 3 ** 235555

@profile
def func_while(n):
    s = ''
    while True:
        s += str(n % 10)
        n //= 10
        if n == 0:
            return s

func_while(n)

@profile
def func_reversed(n):
    return ''.join(reversed(str(n)))

func_reversed(n)

@profile
def func_collection(n):
    return str(n)[::-1]

func_collection(n)

'''
Python 3.7.4
64-разрядная ОС, Win-10

Line #    Mem usage    Increment   Line Contents
================================================
    26     13.3 MiB     13.3 MiB   @profile
    27                             def func_while(n):
    28     13.3 MiB      0.0 MiB       s = ''
    29     13.3 MiB      0.0 MiB       while True:
    30     15.2 MiB  -2177.4 MiB           s += str(n % 10)
    31     15.2 MiB  -2178.7 MiB           n //= 10
    32     15.2 MiB  -2179.0 MiB           if n == 0:
    33     15.2 MiB      0.0 MiB               return s


Line #    Mem usage    Increment   Line Contents
================================================
    37     14.7 MiB     14.7 MiB   @profile
    38                             def func_reversed(n):
    39     14.9 MiB      0.2 MiB       return ''.join(reversed(str(n)))


Line #    Mem usage    Increment   Line Contents
================================================
    43     14.7 MiB     14.7 MiB   @profile
    44                             def func_collection(n):
    45     15.0 MiB      0.3 MiB       return str(n)[::-1]
    
При вводе больших чисел оптимальным алгоритмом является преобразование в строку с обратным выводом.
Примерно тот же результат показывает функция reversed.
Больше всего памяти занимает алгоритм с использованием цикла
'''

