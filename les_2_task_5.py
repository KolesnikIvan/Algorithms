"""5. Вывести на экран коды и символы таблицы ASCII,
начиная с символа под номером 32 и заканчивая 127м включительно.
Вывод выполнить в табличной форме: по 10 пар «код-символ» в каждой строке.
https://github.com/KolesnikIvan/Algorithms/blob/Lesson_2/les_2_task_5.png"""


def print_table(n):
    ten_pares = ''
    global END
    if n + 10 > END:
        lim = END
    else:
        lim = n + 10
    i = n
    while i < lim:
        # ten_pares = ten_pares + str(i) + "-" + str(chr(i)) + ", "
        ten_pares = ten_pares + str(i) + "-" + str(chr(i)) + "\t"
        i = i + 1
    if lim == END:
        ten_pares = ten_pares + str(i) + "-" + str(chr(i)) + "\n"
        return ten_pares
    else:
        ten_pares = ten_pares + "\n"
        return ten_pares + print_table(lim)


BEGIN = 32
END = 127
print(print_table(BEGIN))
