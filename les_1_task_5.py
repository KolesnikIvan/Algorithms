"""5. Пользователь вводит две буквы.
Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
https://github.com/KolesnikIvan/Algorithms/blob/Lesson_1/les_1_task_5.png"""

POS_A = ord('a')
print('Введите две буквы')
smb_1 = str(input('буква 1: '))
smb_2 = str(input('буква 2: '))
cd_1 = ord(smb_1) - POS_A + 1
if smb_1 == smb_2:
    print('Введенные сиволы находятся на месте ', cd_1)
else:
    cd_2 = ord(smb_2) - POS_A + 1
    if cd_1 < cd_2:
        dist = cd_2 - cd_1 - 1
    else:
        dist = cd_1 - cd_2 -1
    print(f'Введенные символы находятся на местах {cd_1} и {cd_2} от начала алгоритма, между ними {dist} букв(ы)')
