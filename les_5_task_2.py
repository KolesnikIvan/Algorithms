"""Написать программу сложения и умножения двух положительных целых шестнадцатеричных чисел.
При этом каждое число представляется как коллекция, элементы которой — цифры числа.
Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’]."""
from collections import deque
from collections import Counter

correspondence = {hex(i).lstrip('0x').capitalize(): i for i in range(1, 16)}
correspond_inv = {i: hex(i).lstrip('0x').capitalize() for i in range(1, 16)}
correspondence['0'] = 0
correspond_inv[0] = '0'

# вводятся исходные данные: два слагаемых
num1_i = list(input('Введите первое шестнадцатиричное число').capitalize())  # list('2A3EF')
num2_i = list(input('Введите второе шестнадцатиричное число').capitalize())  # list('1ED2')
# слагаемые "разворачиваются" для удобства при суммировании
num1 = num1_i[::-1]
num2 = num2_i[::-1]
# по условию задачи слагаемые представляются в виде коллекции-словаря,
# где ключ - номер разаряда слева, но еще преобразую буквы в десятичные цифры
num1c = Counter({i: correspondence[num1[i]] for i in range(len(num1))})
num2c = Counter({i: correspondence[num2[i]] for i in range(len(num2))})

# СЛОЖЕНИЕ
# слагаемые сумимруются в десятичной системе
spam = num1c + num2c
res = deque()
# если цифра в разряде больше шестнадцати, то перенос единицы в старший разряд
for i in range(len(spam) ):
    if spam[i] >= 16:
        spam[i + 1] += 1
        spam[i] = spam[i] - 16
    res.appendleft(correspond_inv[spam[i]])
# если кол-во разрядов увеличилось в результате суммирования, то добавляем 1 вперед
if len(res) < len(spam):
    res.appendleft(correspond_inv[1])
print(''.join(num1_i), "+", ''.join(num2_i), '=', res)

# УМНОЖЕНИЕ
sum_list = []  # это список промежуточных чисел, которые были бы под чертой, если считать столбиком
for j in range(len(num2c)):
    egg = 0  # это произведение двух цифр
    spam = Counter()  # это отдельное такое промежуточное число под чертой
    for i in range(len(num1c)):
        egg += num1c[i] * num2c[j]
        spam[i + j] = egg % 16
        egg = egg // 16
    if egg != 0:
        spam[i + j + 1] = egg
    sum_list.append(spam)

product = deque()
res = Counter()
egg = 0
for spam in sum_list:
    res += spam  # здесь суммируются промежуточные числа
for i in range(len(res)):
    if res[i] >= 16:
        egg = res[i]
        res[i] = egg % 16
        res[i + 1] += egg // 16
    product.appendleft(correspond_inv[res[i]])
if len(res) > len(product): product.appendleft(correspond_inv[res[len(res)]])
print(''.join(num1_i), 'x', ''.join(num2_i), '=', product)
