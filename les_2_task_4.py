"""4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
Количество элементов (n) вводится с клавиатуры.
https://github.com/KolesnikIvan/Algorithms/blob/Lesson_2/les_2_task_4.png"""


def series_summ(n):
    if n > 1:
        return (-1)**(n-1) * 0.5**(n-1) + series_summ(n-1)
    else:
        return (-1) ** (n - 1) * 0.5 ** (n - 1)


print('Введите количество элементов ряда')
n = int(input())
S = series_summ(n)
print(S)
