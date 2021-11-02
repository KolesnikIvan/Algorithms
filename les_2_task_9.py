"""9. Среди натуральных чисел, которые были введены,
найти наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
https://github.com/KolesnikIvan/Algorithms/blob/Lesson_2/les_2_task_9.png"""


def s_digit(n):
    if n < 10:
        return n
    else:
        return n % 10 + s_digit(n // 10)


n_max = 0; s_max = 0
while True:
    print('Введите натуральное число ')
    n = int(input())
    if n != 0:
        s = s_digit(n)
        if s > s_max:
            n_max = n
            s_max = s
    else:
        print('Ввод ', n, ' означает завершение работы')
        if s_max != 0:
            print('Число с наибольшей суммой цифр ', n_max, ', сумма цифр ', s_max, '.')
        else:
            print('Не было введено ни одного числа.')
        break
