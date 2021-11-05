"""4.	Определить, какое число в массиве встречается чаще всего. """
import random

SIZE = 100
MIN_ITEM = 10
MAX_ITEM = 30
arr = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(arr)

unique = set(arr)
# почему-то следующая строка не сработала
# dict_cnt = {el: sum(1 if el == i else 0) for i in arr for el in unique}
mx = 0; mx_el = arr[0]
for spam in unique:
    cnt = 0
    for egg in arr:
        if spam == egg:
            cnt += 1
    if mx < cnt:
        mx = cnt
        mx_el = spam
print('Наиболее часто в массиве встречается элемент', mx_el)
