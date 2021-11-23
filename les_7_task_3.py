"""3). Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные
части: в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы."""
import random

M = 7
MAX_ITEM = 20
array = [random.randint(1, MAX_ITEM) for _ in range(2 * M + 1)]


def gnom_sort(arr):
    i = 0
    while i < len(arr):
        if i > 0:
            if arr[i] >= arr[i - 1]:
                i += 1
            else:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                i -= 1
        else:
            i += 1
    return arr


print('Исходный массив ', array)
array_s = gnom_sort(array)
print('Отсортированный ', array_s)
print('Медиана ', array_s[len(array_s) // 2])
