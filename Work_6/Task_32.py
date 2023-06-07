#Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
import random

lst = [random.randint(-15, 15) for _ in range(10)]
print(lst)
min_number = int(input())
max_number = int(input())
for i in range(len(lst)):
    if min_number <= lst[i] <= max_number:
        print(i)