"""2). Отсортируйте по возрастанию методом слияния одномерный вещественный
массив, заданный случайными числами на промежутке [0; 50).
Выведите на экран исходный и отсортированный массивы."""
import random

SIZE = 10
array = [50 * random.random() for _ in range(SIZE)]


def confluence_sort(arr):
    if len(arr) == 1:
        return arr
    elif len(arr) == 2:
        if arr[0] > arr[1]:
            arr[0], arr[1] = arr[1], arr[0]
        return arr

    else:
        egg = len(arr) // 2
        arr1, arr2 = arr[: egg], arr[egg:]
        arr1 = confluence_sort(arr1)
        arr2 = confluence_sort(arr2)

        res = []
        idx1 = idx2 = 0
        spam = []
        for i in range(len(arr1) + len(arr2)):
            if idx1 > len(arr1) - 1:
                res.append(arr2[idx2])
                idx2 += 1
            elif idx2 > len(arr2) - 1:
                res.append(arr1[idx1])
                idx1 += 1

            elif arr1[idx1] < arr2[idx2]:
                res.append(arr1[idx1])
                idx1 += 1
            else:
                res.append(arr2[idx2])
                idx2 += 1

        return res


print('Исходный массив ', array)
array_s = confluence_sort(array)
print('Отсортированный ', array_s)
