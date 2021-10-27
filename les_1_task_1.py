"""1. Найти сумму и произведение цифр трехзначного числа,
которое вводит пользователь.
https://github.com/KolesnikIvan/Algorithms/blob/Lesson_1/les_1_task_1.png"""

print('Введите целое трехзначеное число ')
num = int(input())
d1 = num // 100
num = num % 100
d2 = num // 10
num = num % 10
prod = d1 * d2 * num
summ = d1 + d2 + num
print('Произведение цифр равно ', prod)
print('Сумма цифр равна ', summ)
