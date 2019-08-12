"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
"""

"""
Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
"""
import timeit

def cycle(n, even, odd):
    while n > 0:
        if n % 2 == 0:
            even += 1
        else:
            odd += 1
        n = n // 10

def recursion(num, even=0, odd=0):
    if num == 0:
        return even, odd
    else:
        n = num % 10
        num = num // 10
        if n % 2 == 0:
            even += 1
            return recursion(num, even, odd)
        else:
            odd += 1
            return recursion(num, even, odd)

print(timeit.timeit("recursion(978968367,0,0)", setup="from __main__ import recursion", number=1))
print(timeit.timeit("cycle(978968367,0,0)", setup="from __main__ import cycle", number=1))

"""
Время выполнения функций:
3.5922999999993266e-05 - recursion
1.7727999999994637e-05 - cycle
Время выполнения функции с помощью рекурсии больше, т.к. происходит многократный вызов функции.
В цикле же происходит лишь один вызов функции и последовательное выполнение простейших операций.
В обоих случаях имеем дело с линейной сложностью O(n).
Время выполнения будет увеличиваться с увеличением цифр в заданном числе.
"""