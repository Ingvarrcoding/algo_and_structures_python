"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры
числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и
[‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

import collections

def get_result():
    input_num = input('Введите два числа в шестнадцатеричном формате через пробел: ').split()
    numbers = collections.defaultdict(list)
    for num in input_num:
        numbers[num] = list(num)
    sum_num = 0
    mul_num = 1
    for num in numbers.keys():
        num = int(num, 16)
        sum_num += num
        mul_num *= num
    sum_num = list(hex(sum_num).upper())[2:]
    mul_num = list(hex(mul_num).upper())[2:]
    return sum_num, mul_num

def main():
    try:
        sum_num, mul_num = get_result()
        print()
        print(f'Сумма чисел {sum_num} \nПроизведение {mul_num}')
    except ValueError:
        print()
        print('Неверный формат')

main()

'''
Введите два числа в шестнадцатеричном формате через пробел: A2 C4F

Сумма чисел ['C', 'F', '1'] 
Произведение ['7', 'C', '9', 'F', 'E']

----------------------------------------------------------------------

Введите два числа в шестнадцатеричном формате через пробел: A2 и C4F

Неверный формат
'''