"""3. По введенным пользователем координатам двух точек
вывести уравнение прямой вида y = kx + b, проходящей через эти точки.
https://github.com/KolesnikIvan/Algorithms/blob/Lesson_1/les_1_task_3.png"""

print("Введите координаты двух точек")
x1 = float(input('x1 = '))
y1 = float(input('y1 = '))
x2 = float(input('x2 = '))
y2 = float(input('y2 = '))
if x1 == x2:
    print('Уравнение прямой x = ', x1)
else:
    k = (y2-y1) / (x2-x1)
    b = (x2*y1 - x1*y2) / (x2-x1)
    if b > 0:
        print('Уравнение прямой y = %4.2f*x+%4.2f' % (k, b))
    else:
        print('Уравнение прямой y = %4.2f*x-%4.2f' % (k, -b))
