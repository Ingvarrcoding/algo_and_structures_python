"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.
"""

import random

size = int(input('Введите длину массива: '))
array = [round(random.uniform(1, 50,), 2) for i in range(size)]
print (f'Исходный массив: {array}')

def merge_sort(array):
    length = len(array)
    if length > 1:
        mid = length // 2
        left = array[:mid]
        right = array[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
    return array

merge_sort(array)

print(f'Массив, отсортированный по возрастанию: {array}')

'''
Введите длину массива: 10
Исходный массив: [47.38, 9.62, 23.65, 18.32, 40.13, 45.02, 26.36, 33.33, 40.27, 20.12]
Массив, отсортированный по возрастанию: [9.62, 18.32, 20.12, 23.65, 26.36, 33.33, 40.13, 40.27, 45.02, 47.38]
'''

