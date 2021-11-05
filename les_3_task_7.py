"""7.	В одномерном массиве целых чисел определить два наименьших
элемента. Они могут быть, как равны, так и различаться. """
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
arr = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
# arr =[79, 29, 83, 63, 32, 48, 79, 37, 30, 53]
print(arr)

mn1 = mn2 = MAX_ITEM
for el in arr:
    if mn1 > el:
        mn2 = mn1
        mn1 = el
    elif mn2 > el and mn2 >= mn1:
        mn2 = el
print('Два наименьших элемента массива - это', mn1, 'и', mn2)
