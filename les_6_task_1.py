"""6.	В одномерном массиве найти сумму элементов междуу максимальным
и минимальным элеменитами. Сами максимальный и минимальный в сумму не включать. """
import random
from collections import deque
import sys
import inspect

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
arr = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]


def var_1(array: list):
    pos_mx = pos_mn = 0
    mn = mx = array[0]
    for i in range(1, len(array)):
        if array[i] < mn:
            mn = array[i]
            pos_mn = i
        if array[i] > mx:
            mx = array[i]
            pos_mx = i
    if pos_mn > pos_mx:
        pos_mn, pos_mx = pos_mx, pos_mn
    s = 0
    for el in array[pos_mn+1:pos_mx]:
        s += el
    print('v1. Сумма элементов ', s)
    report = []
    for i in locals().copy():
        if not (i.startswith('_') or hasattr(eval(i), 'call')):
            report.append({'proc': inspect.currentframe().f_code.co_name, 'name': i, 'type': type(eval(i)),
                           'size': sys.getsizeof(eval(i))})
            # report.append({'name':i, 'type': type(eval(i)), 'size': sys.getsizeof(eval(i))}})
    return report

def var_1_1(array: list):
    mn = array.index(min(array))
    mx = array.index(max(array))
    if mn > mx:
        mn, mx = mx, mn
    s = sum(array[mn+1:mx])
    print('v1_1. Сумма элементов ', s)
    report = []
    for i in locals().copy():
        if not (i.startswith('_') or hasattr(eval(i), 'call') or i == 'report'):
            report.append({'proc': 'var_1_1', 'name': i, 'type': type(eval(i)),
                           'size': sys.getsizeof(eval(i))})
            # report.append({i:{'name':i, 'type': type(eval(i)), 'size': sys.getsizeof(eval(i))}})
    return report


def var_2(array: list):
    dq = deque(array)
    mn = dq.index(min(dq))
    mx = dq.index(max(dq))
    if mn > mx:
        mn, mx = mx, mn
    s = 0
    for i in range(mn + 1, mx):
        s += dq[i]
    print('v2. Сумма элементов ', s)
    report = []
    for i in locals().copy():
        if not (i.startswith('_') or hasattr(eval(i), 'call') or i == 'report'):
            report.append({'proc': 'var_2', 'name': i, 'type': type(eval(i)),
                           'size': sys.getsizeof(eval(i))})
            # report.append({i:{'name':i, 'type': type(eval(i)), 'size': sys.getsizeof(eval(i))}})
    return report


def var_3(array: list):
    array = list(map(str, array))
    mn = array.index(min(array))
    mx = array.index(max(array))
    if mn > mx:
        mn, mx = mx, mn
    s = 0
    for i in range(mn + 1, mx):
        s += int(array[i])
    print('v3. Сумма элементов ', s)

    report = []
    for i in locals().copy():
        if not (i.startswith('_') or hasattr(eval(i), 'call') or i == 'report'):
            report.append({'proc': 'var_3', 'name': i, 'type': type(eval(i)),
                           'size': sys.getsizeof(eval(i))})
    return report
    # return \
    #     [{'proc': 'var_3', 'name': i, 'type': type(eval(i)), 'size': sys.getsizeof(eval(i))}
    #     for i in locals().copy() if not (i.startswith('_') or hasattr(eval(i), 'call'))]


rep = []
print(arr)
rep.extend(var_1(arr))
rep.extend(var_1_1(arr))
rep.extend(var_2(arr))
rep.extend(var_3(arr))
print(*rep, sep='\n')

# Тип системы: 64-разраядная операционная система, процессор х64.
# Python 3.8.7 (tags/v3.8.7:6503f05, Dec 21 2020, 17:59:51) [MSC v.1928 64 bit (AMD64)] on win32
#
# [20, 13, 38, 81, 41, 23, 85, 24, 93, 56]
# v1. Сумма элементов  292;     занято 522 (402) байта
# v1_1. Сумма элементов  292;   занято 268 байт
# v2. Сумма элементов  292;     занято 942 байта
# v3. Сумма элементов  292;     занято 286 байт

# Вывод (на основании цифр ниже).
# Простой перебор массива для поиска индексов и еще один перебор для суммирования показывают
# неплохие результаты (занимают не самый большой объем памяти, тем более, что там переменная report лишняя,
# но ее удаление распределения мест не изменит).
# Самый экономный вариант - использование встроенных функций. В третьем варианте массив хоть и показан,
# как class int (почему?), все же занимает меньше места чем аналогичные структуры в других вариантах.
# Последняя реализация почему-то иногда дает результаты, отличающиеся от других.

# {'proc': 'var_1', 'name': 'array', 'type': <class 'list'>, 'size': 184}
# {'proc': 'var_1', 'name': 'pos_mx', 'type': <class 'int'>, 'size': 28}
# {'proc': 'var_1', 'name': 'pos_mn', 'type': <class 'int'>, 'size': 28}
# {'proc': 'var_1', 'name': 'mn', 'type': <class 'int'>, 'size': 28}
# {'proc': 'var_1', 'name': 'mx', 'type': <class 'int'>, 'size': 28}
# {'proc': 'var_1', 'name': 'i', 'type': <class 'str'>, 'size': 50}
# {'proc': 'var_1', 'name': 's', 'type': <class 'int'>, 'size': 28}
# {'proc': 'var_1', 'name': 'el', 'type': <class 'int'>, 'size': 28}
# {'proc': 'var_1', 'name': 'report', 'type': <class 'list'>, 'size': 120}
# {'proc': 'var_1_1', 'name': 'array', 'type': <class 'list'>, 'size': 184}
# {'proc': 'var_1_1', 'name': 'mn', 'type': <class 'int'>, 'size': 28}
# {'proc': 'var_1_1', 'name': 'mx', 'type': <class 'int'>, 'size': 28}
# {'proc': 'var_1_1', 'name': 's', 'type': <class 'int'>, 'size': 28}
# {'proc': 'var_2', 'name': 'array', 'type': <class 'list'>, 'size': 184}
# {'proc': 'var_2', 'name': 'dq', 'type': <class 'collections.deque'>, 'size': 624}
# {'proc': 'var_2', 'name': 'mn', 'type': <class 'int'>, 'size': 28}
# {'proc': 'var_2', 'name': 'mx', 'type': <class 'int'>, 'size': 28}
# {'proc': 'var_2', 'name': 's', 'type': <class 'int'>, 'size': 28}
# {'proc': 'var_2', 'name': 'i', 'type': <class 'str'>, 'size': 50}
# {'proc': 'var_3', 'name': 'array', 'type': <class 'list'>, 'size': 152}
# {'proc': 'var_3', 'name': 'mn', 'type': <class 'int'>, 'size': 28}
# {'proc': 'var_3', 'name': 'mx', 'type': <class 'int'>, 'size': 28}
# {'proc': 'var_3', 'name': 's', 'type': <class 'int'>, 'size': 28}
# {'proc': 'var_3', 'name': 'i', 'type': <class 'str'>, 'size': 50}
#
# Process finished with exit code 0
