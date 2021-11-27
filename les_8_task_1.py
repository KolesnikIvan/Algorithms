"""1) Определение количества различных подстрок с использованием
хеш-функции.
Пусть на вход функции дана строка.
Требуется вернуть количество различных подстрок в этой строке.
Примечание: в сумму не включаем пустую строку и строку целиком."""
import random
import string

SIZE = 11
str_to_hash = ''.join(random.choice(string.ascii_lowercase) for _ in range(SIZE))


def hash_substring(text):
    substrings = set()
    n = 0
    while n < len(text):
        for i in range(n+1, len(text)+1):
            substrings.add(text[n:i])

        n += 1
    substrings.discard(text)
    # substrings.discard('')
    return len(substrings)  # , substrings


print('Исходная строка', str_to_hash)
print('Хешированная ', hash_substring(str_to_hash))
print('Проверка sova', hash_substring('sova'))
print('Проверка papa', hash_substring('papa'))
