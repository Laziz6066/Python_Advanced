"""
Вася решил передать Пете шифрограмму.
Поскольку о промышленных шифрах Вася ничего не знает,
он решил зашифровать сообщение следующим образом: он посылает Пете строку.

Каждый символ строки — либо буква, либо пробел, либо точка «.», либо две точки «..».
Если после какой-то буквы стоит точка, значит, мы оставляем букву без изменений
(об одной точке Вася задумался, чтобы усложнить расшифровку). Саму точку при этом надо удалить.
Если после какой-то буквы стоят две точки, то предыдущий символ надо стереть. Обе точки при этом тоже нужно удалить.
Возможна ситуация, когда сообщение после расшифровки будет пустым.
В качестве результата можно вернуть просто пустую строку.

Примеры шифровок-расшифровок:

абра-кадабра. → абра-кадабра
абраа..-кадабра → абра-кадабра
абраа..-.кадабра → абра-кадабра
абра--..кадабра → абра-кадабра
абрау...-кадабра → абра-кадабра (сначала срабатывает правило двух точек, потом правило одной точки)
абра........ → <пустая строка>
абр......a. → a
1..2.3 → 23
. → <пустая строка>
1....................... → <пустая строка>

Помогите Пете написать программу для расшифровки.
Напишите функцию decrypt, которая принимает на вход шифр в виде строки, а возвращает расшифрованное сообщение.

Программа должна работать через конвейер (pipe):

$ echo  ‘абраа..-.кадабра’ | python3 decrypt.py
абра-кадабра

Команда echo выводит текст (в стандартный поток вывода).
"""

import sys


def decrypt(encryption: str) -> str:
    result = []
    i = 0
    while i < len(encryption):
        if encryption[i] == '.':
            i += 1
        elif i < len(encryption) - 1 and encryption[i:i + 2] == '..':
            if len(result) > 0:
                result.pop()
            i += 2
        else:
            result.append(encryption[i])
            i += 1
    return ''.join(result)


if __name__ == '__main__':
    data: str = sys.stdin.read()
    decryption: str = decrypt(data)
    print(decryption)
