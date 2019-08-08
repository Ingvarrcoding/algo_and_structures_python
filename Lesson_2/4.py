"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
"""

'''
n = int(input())
e = 1
s = 0
for i in range(n):
    s += e
    e /= -2
print(s)
'''

def recursion(i, num, n, summ):
    if i == n:
        return summ
    elif i < n:
        return recursion(i+1, num/(-2), n, summ+num)
n = int(input("Введите количество элементов: "))
print(recursion(0, 1, n, 0))