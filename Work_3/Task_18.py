#Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

import random

N = int(input("Введите количество элементов в массиве "))
list = [random.randint(1, 20) for i in range(N)]
print(list)
x = int(input("Введите искомое число "))
index_element = 0
min_element = abs(x - list[0])
for i in range(1, N):
    buffer_element = abs(x -list[i])
    if buffer_element < min_element:
        min_element = buffer_element
        index_element = i

print(f"Самый близкий по величине элемент к заданному числу {list[index_element]}")