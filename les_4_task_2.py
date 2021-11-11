"""
2). Написать два алгоритма нахождения i-го по счёту простого числа.
Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
Проанализировать скорость и сложность алгоритмов.

Первый — с помощью алгоритма «Решето Эратосфена».
Второй — без использования «Решета Эратосфена».
"""
import cProfile
import timeit
import math


def sieve_les_2(i):
    # задаемся размером решета
    # https://ru.wikipedia.org/wiki/%D0%A7%D0%B8%D1%81%D0%BB%D0%BE_%D0%9C%D0%B5%D1%80%D1%81%D0%B5%D0%BD%D0%BD%D0%B0
    if i == 1:
        return 2
    else:
        spam = 0
        while True:
            n = 2**(i+spam) - 1
            sieve = [k for k in range(n)]
            sieve[0] = 0
            for k in range(2, n):
                if sieve[k] != 0:
                    j = k + k
                    while j < n:
                        sieve[j] = 0
                        j += k
            res = [k for k in sieve if k != 0]

            if len(res) >= i:
                return res[i-1]
            elif spam > 20:
                # raise StopIteration(f'{i}th prime number not found')
                return f'{i}th prime number not found'
            else:
                # если на заданном отрезке не найдено нужного количества простых,
                # увеличить отрезок и начать с начала
                spam += 1


def prime_les_4(i):
    if i == 1:
        return 2
    else:
        cnt = 1
        res = num = 2
        while cnt < i:
            num += 1
            lim = math.ceil(math.sqrt(num)) + 1
            # прочитал, что можно проверять делители до корня из анализируемого числа
            # http://mech.math.msu.su/~shvetz/54/inf/perl-problems/chPrimes_sIdeas.xhtml
            is_prime = True
            for j in range(2, lim):
                if num % j == 0:
                    is_prime = False
                    break
            if is_prime:
                res = num
                cnt += 1
        return res


variants = ['sieve_les_2(', 'prime_les_4(']
# сравнение
msrmnts = 1000
size = 18
with open('compare2.txt', mode='w', encoding='utf-8') as fl:
    for var in variants:
        for i in range(5, size, 2):
            func = var + str(i) + ')'
            try:
                tm = str(timeit.timeit(func, number=msrmnts, globals=globals()))
            except Exception as expt:
                tm = str(expt)
                pass
            fl.write('|'.join([func, tm, '\n']))

        fl.write('*' * 10 + '\n')

for var in variants:
    func = var + str(size) + ')'
    try:
        print(func)
        cProfile.run(func)  # , fl.name)
    except Exception as expt:
        fl.write('cProf' + func + ' ' + str(expt))
        continue
    # fl.write('*' * 20 + '\n')

# sieve_les_2(18)
#          7 function calls in 0.133 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.004    0.004    0.133    0.133 <string>:1(<module>)
#         1    0.098    0.098    0.129    0.129 les_4_task_2.py:14(sieve_les_2)
#         1    0.020    0.020    0.020    0.020 les_4_task_2.py:23(<listcomp>)
#         1    0.010    0.010    0.010    0.010 les_4_task_2.py:31(<listcomp>)
#         1    0.000    0.000    0.133    0.133 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
# prime_les_4(18)
#          122 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 les_4_task_2.py:44(prime_les_4)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        59    0.000    0.000    0.000    0.000 {built-in method math.ceil}
#        59    0.000    0.000    0.000    0.000 {built-in method math.sqrt}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# Process finished with exit code 0
