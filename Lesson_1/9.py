# 9.Вводятся три разных числа. Найти, какое из них
# является средним (больше одного, но меньше другого).

print("Введите три числа: ")
a = int(input())
b = int(input())
c = int(input())
if a == b or a == c or b == c:
    print("Нет среднего числа")
elif b < a < c or c < a < b:
    print("Среднее: ", a)
elif a < b < c or c < b < a:
    print("Среднее: ", b)
else:
    print("Среднее: ", c)

