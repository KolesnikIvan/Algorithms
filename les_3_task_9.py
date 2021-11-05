"""9.	Найти максимальный среди минимальных элементов столбцов матрицы. """
import random

ROWS = 4
COLUMNS = 4
MIN_ITEM = 0
MAX_ITEM = 100
arr = [[random.randint(MIN_ITEM, MAX_ITEM) for _ in range(COLUMNS)]
       for _ in range(ROWS)]
print(*arr, sep='\n')

arr_mn = [MAX_ITEM for _ in range(COLUMNS)]
mx = MIN_ITEM
for j in range(COLUMNS):
    for i in range(ROWS):
        if arr_mn[j] > arr[i][j]:
            arr_mn[j] = arr[i][j]
    if mx < arr_mn[j]:
        mx = arr_mn[j]
print('Максимальный среди минимальных элементов столбцов ', mx)
