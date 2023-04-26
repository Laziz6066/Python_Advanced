"""
Удобно направлять результат выполнения команды напрямую в программу с помощью конвейера (pipe):

$ ls -l | python3 get_mean_size.py

Напишите функцию get_mean_size, которая на вход принимает результат выполнения команды ls -l,
а возвращает средний размер файла в каталоге.
"""

import sys


def get_mean_size(ls_output: str) -> float:

    ls_output = ls_output[1:]
    total_size = 0
    num_files = 0
    for line in ls_output:

        fields = line.split()
        if len(fields) > 4:

            size = int(fields[4])
            total_size += size
            num_files += 1
    if num_files == 0:
        return 0
    return total_size / num_files


if __name__ == '__main__':
    data: str = sys.stdin.read()
    mean_size: float = get_mean_size(data)
    print(mean_size)
