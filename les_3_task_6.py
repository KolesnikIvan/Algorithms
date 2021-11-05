"""6.	В одномерном массиве найти сумму элементов междуу максимальным
и минимальным элеменитами. Сами максимальный и минимальный в сумму не включать. """
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
arr = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(arr)

pos_mx = pos_mn = 0
mn = mx = arr[0]
for i in range(1, len(arr)):
    if arr[i] < mn:
        mn = arr[i]
        pos_mn = i
    if arr[i] > mx:
        mx = arr[i]
        pos_mx = i
if pos_mn > pos_mx:
    pos_mn, pos_mx = pos_mx, pos_mn
s = 0
for el in arr[pos_mn+1:pos_mx]:
    s += el
print('Сумма элементов ', s)
