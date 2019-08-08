"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.
"""

'''
n = int(input())
s = 0
for i in range(1,n+1):
    s += i
m = n * (n + 1) // 2
print(s)
print(m)
'''

def teorema(n, s=0, m=1):
    if s == m:
        return f"Равенство: {s == m}, {s}, {m}"
    elif s < m:
        return teorema(n, s+1, n * (n + 1) // 2)
n = int(input("Введите число: "))
print(teorema(n))
