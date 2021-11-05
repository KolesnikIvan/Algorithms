"""1.	В диапазоне натуральных чисел от 2 до 99 определить,
сколько кратны каждому из чисел в диапазоне от 2 до 9."""

nat_nums = dict.fromkeys((2, 3, 4, 5, 6, 7, 8, 9))
for num in nat_nums:
    cnt = 0
    for i in range(num, 99 + 1, num):
        if i % num == 0:
            cnt += 1
    nat_nums[num] = cnt
print(nat_nums)
# ключи массива nat_nums - это нат.числа от 2 до 9 включительно
# значения массива - это количество чисел, кратных ключу
