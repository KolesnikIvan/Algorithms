"""8. Определить, является ли год, который ввел пользователь,
високосным или невисокосным.
https://github.com/KolesnikIvan/Algorithms/blob/Lesson_1/les_1_task_8.png"""

print('Введите номер года')
yr = int(input('year:'))
if yr % 4 == 0:
    if yr % 100 != 0:
        print('Год високосный')
    elif yr % 400 == 0:
        print('Год високосный')
    else:
        print('Год невисокосный')
else:
    print('Год не високосный')
