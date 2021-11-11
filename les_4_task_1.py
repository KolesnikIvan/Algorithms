"""1). Проанализировать скорость и сложность одного любого
алгоритма из разработанных в рамках домашнего задания первых трех уроков.

Использую задачу 4 из урока 2 про геометрическую прогрессию

4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
Количество элементов (n) вводится с клавиатуры.
https://github.com/KolesnikIvan/Algorithms/blob/Lesson_2/les_2_task_4.png"""
import timeit
import cProfile
# import profile


# вариант базовый
def recursive_sum(n):
    if n > 1:
        return (-1)**(n-1) * 0.5**(n-1) + recursive_sum(n-1)
    else:
        return (-1) ** (n - 1) * 0.5 ** (n - 1)


# вариант в лоб
def simple_sum(n):
    sum_ = 0
    for i in range(n):
        sum_ += 1/((-2) ** i)
    return sum_


# вариант по школьной формуле
def progress_sum(n):
    b1 = 1
    q =-0.5
    return b1 * (q**n - 1) / (q - 1)


# вариант со списком
def list_sum(n):
    b1 = 1
    q = -0.5
    series = [b1 * q**(i-1) for i in range(n)]
    return sum(series)


variants = ['simple_sum(', 'progress_sum(', 'list_sum(']
# сравнение
msrmnts = 1000
elements = 6
basis = 8
with open('compare1.txt', mode='w', encoding='utf-8') as fl:
    for var in variants:
        for i in range(1, elements):
            spam = str(basis ** i)
            func = var + spam + ')'
            try:
                tm = str(timeit.timeit(func, number=msrmnts, globals=globals()))
            except Exception as expt:
                tm = str(expt)
                pass
            fl.write('|'.join([func, tm, '\n']))

        fl.write('*' * 10 + '\n')

for var in variants:
    spam = str(basis ** elements-1)
    func = var + spam + ')'
    try:
        print(func)
        cProfile.run(func)
        # cProfile.run(func, fl.name)
        # profile.run(func, fl.name)
    except Exception as expt:
        fl.write('cProf' + func + ' ' + str(expt))
        continue
    # fl.write('*' * 20 + '\n')

# simple_sum(32768)
#          4 function calls in 1.671 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    1.671    1.671 <string>:1(<module>)
#         1    1.671    1.671    1.671    1.671 les_4_task_1.py:23(simple_sum)
#         1    0.000    0.000    1.671    1.671 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
# progress_sum(32768)
#          4 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 les_4_task_1.py:31(progress_sum)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
# list_sum(32768)
#          6 function calls in 0.012 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.001    0.001    0.012    0.012 <string>:1(<module>)
#         1    0.000    0.000    0.011    0.011 les_4_task_1.py:38(list_sum)
#         1    0.011    0.011    0.011    0.011 les_4_task_1.py:41(<listcomp>)
#         1    0.000    0.000    0.012    0.012 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.sum}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
#
# Process finished with exit code 0
