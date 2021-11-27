"""2) Закодируйте любую строку по алгоритму Хаффмана.
Превратитет строку текста в строку из нулей и единиц -
визуальное текстовое представление сжатие данных."""
import random
import string
from collections import Counter


SIZE = 10
# str_to_archive = ''.join(random.choice(string.ascii_lowercase) for _ in range(SIZE))
str_to_archive = 'beep boop beer!'

class Node:

    def __init__(self, left=None, right=None, value=None, step=None, letter=None):
        self.step = step
        self.letter = letter
        self.left = left
        self.right = right
        self.value = value

    def __repr__(self):
         return f'Node[{self.letter}, {self.value}]'  # , {self.left}, {self.right}]'


def find_letter(nd, letter, code_str=''):
    # проходит по узлам в поисках букв
    if nd.letter == letter:
        return code_str
    elif nd.left is not None and nd.left.letter == letter:
        return ''.join([code_str, '0'])
    elif nd.right is not None and nd.right.letter == letter:
        return ''.join([code_str, '1'])
    else:
        if nd.left is not None:
            str_s = find_letter(nd.left, letter, code_str)
            if str_s != '':
                return ''.join([str_s, '0'])
            else:
                if nd.right is not None:
                    str_s = find_letter(nd.right, letter, code_str)
                    if str_s != '':
                        return ''.join([str_s, '1'])
                    else:
                        return ''
                return ''
        else:
            return ''


frequency_c = Counter(str_to_archive).most_common()        # получить частоты символов

nds = []  # первоначально заполнить массив узлов
for i in frequency_c:
    nds.append(Node(letter=i[0], value=i[1]))
# for i in range(len(nds)):
i = -1
while len(nds) > 1:  # объединять узлы от меньших частот к большим
    nd_l = nds.pop()
    nd_r = nds.pop()
    nd = Node(step=i, left=nd_l, right=nd_r, value=nd_l.value + nd_r.value)
    j = -1
    while j >= -len(nds):
        if nds[j].value >= nd.value:
            break
        j += -1
    nds.insert(j, nd)
    i += -1

nd = nds[0]


code_str = ''  # пройти по полученному дереву в поисках каждого символа исходной строки
for smb in str_to_archive:
    smb_code = find_letter(nd, smb)
    code_str += smb_code

print('Исходная строка ', str_to_archive, len(str_to_archive))
print('Закодированная ', code_str, len(code_str))
b_str_to_archive = ''.join(format(ord(smb), 'b') for smb in str_to_archive)
print('Двоичная ', b_str_to_archive, len(b_str_to_archive))
