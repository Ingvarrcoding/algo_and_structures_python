"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.
"""

'''
n = int(input())
m = 0
while n>0:
    m = m*10 + n%10
    n = n//10
print(m)
'''

def flip_num(num, flip=0):
    if num == 0:
        return flip
    else:
        flip = (flip * 10) + (num % 10)
        num = num // 10
        return flip_num(num, flip)
num = int(input("Введите число, которое требуется перевернуть: "))
print(f"Перевернутое число: {flip_num(num)}")
