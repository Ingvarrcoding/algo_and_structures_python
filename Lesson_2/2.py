"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
"""

'''
n = int(input())
even=odd=0
while n>0:
    if n%2 == 0:
        even += 1
    else:
        odd += 1
    n = n//10
print("четных - %d, нечетных - %d" % (even, odd))
'''

def cnt_even_odd(num, even=0, odd=0):
        if num == 0:
                return even, odd
        else:
                n = num % 10
                num = num // 10
                if n % 2 == 0:
                        even += 1
                        return cnt_even_odd(num, even, odd)
                else:
                        odd += 1
                        return cnt_even_odd(num, even, odd)
num = int(input("Введите число: "))
print(f"Количество четных и нечетных цифр в числе равно: {cnt_even_odd(num)}")
