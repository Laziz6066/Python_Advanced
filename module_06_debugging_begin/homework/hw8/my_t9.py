"""
У нас есть кнопочный телефон (например, знаменитая Nokia 3310), и мы хотим,
чтобы пользователь мог проще отправлять СМС. Реализуем своего собственного клавиатурного помощника.

Каждой цифре телефона соответствует набор букв:
* 2 — a, b, c;
* 3 — d, e, f;
* 4 — g, h, i;
* 5 — j, k, l;
* 6 — m, n, o;
* 7 — p, q, r, s;
* 8 — t, u, v;
* 9 — w, x, y, z.

Пользователь нажимает на клавиши, например 22736368, после чего на экране печатается basement.

Напишите функцию my_t9, которая принимает на вход строку, состоящую из цифр 2–9,
и возвращает список слов английского языка, которые можно получить из этой последовательности цифр.
"""
from typing import List
import re


def my_t9(input_numbers: str) -> List[str]:
    with open('/usr/share/dict/words', 'r') as f:
        dictionary = set(word.strip().lower() for word in f)

    digit_mapping = {
        '2': '[abc]',
        '3': '[def]',
        '4': '[ghi]',
        '5': '[jkl]',
        '6': '[mno]',
        '7': '[pqrs]',
        '8': '[tuv]',
        '9': '[wxyz]'
    }

    pattern = ''.join(digit_mapping.get(digit, '') for digit in input_numbers)
    regex = re.compile(pattern)

    results = [word for word in dictionary if regex.match(word)]
    return results


if __name__ == '__main__':
    numbers: str = input()
    words: List[str] = my_t9(numbers)
    print(*words, sep='\n')
