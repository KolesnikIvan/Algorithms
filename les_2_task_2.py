"""2.Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, в нем три четные цифры (4, 6, 0)
и две нечетные (3 и 5).
https://github.com/KolesnikIvan/Algorithms/blob/Lesson_2/les_2_task_2.png"""


def digits_counter(num, even):
    if num < 10:
        if num % 2 == 0 and even \
                or num %2 != 0 and not even:
            return 1
        else:
            return 0

    else:
        dgt = num % 10
        num = num // 10

        if dgt % 2 == 0 and even\
                or num %2 !=0 and not even:
            return 1 + digits_counter(num, even)
        else:
            return digits_counter(num, even)


print('Введите натуральное число ')
num = int(input())
odd = 0
even = 0
even = digits_counter(num, True)
odd = digits_counter(num, False)
print('Во введенном числе ', odd, ' нечетных цифр(ы) и ', even, ' четных.')
