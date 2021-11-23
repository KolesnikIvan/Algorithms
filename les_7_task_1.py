"""1. Отсортируйте по убыванию методом пузырька одномерный целочисленый массив, заданный случайными числами
на промежутке [-100;100). Выведите на экран исходный и отсортированный массивы.
Сортировка должна быть реализована в иде функции. """
import random

SIZE = 10
array = [random.randint(-100, 99) for _ in range(SIZE)]


def is_sorted(arr):
    is_sorted = True
    for i in range(len(arr)-1):
        if arr[i] < arr[i + 1]:
            is_sorted = False
            break
    return is_sorted


def bubble_sort(arr):
    n = 0
    while n < len(arr):
        for i in range(len(arr) - 1, n, -1):
            if arr[i] > arr[i-1]:
                arr[i], arr[i-1] = arr[i-1], arr[i]
        n += 1
        if is_sorted(arr):
            break
    return arr


print('Исходный массив ', array)
array_s = bubble_sort(array)
print('Отсортированный ', array_s)
