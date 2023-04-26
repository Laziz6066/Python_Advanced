"""
С помощью команды ps можно посмотреть список запущенных процессов.
С флагами aux эта команда выведет информацию обо всех процессах, запущенных в системе.

Запустите эту команду и сохраните выданный результат в файл:

$ ps aux > output_file.txt

Столбец RSS показывает информацию о потребляемой памяти в байтах.

Напишите функцию get_summary_rss, которая на вход принимает путь до файла с результатом выполнения команды ps aux,
а возвращает суммарный объём потребляемой памяти в человекочитаемом формате.
Это означает, что ответ надо перевести в байты, килобайты, мегабайты и так далее.
"""
from flask import Flask
import os


app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RSS_FILE = os.path.join(BASE_DIR, 'output_file.txt')


@app.route("/output_file/<path:ps_output_file_path>")
def get_summary_rss(ps_output_file_path: str) -> str:
    with open(ps_output_file_path, 'r') as f:
        lines = f.readlines()[1:]
        rss_sum = sum(int(line.split()[5]) for line in lines)
        suffixes = ['B', 'KiB', 'MiB', 'GiB', 'TiB', 'PiB']
        index = 0
        while rss_sum >= 1024 and index < len(suffixes) - 1:
            rss_sum /= 1024
            index += 1
        return f"Memory consumption: {rss_sum:.2f} {suffixes[index]}"



if __name__ == '__main__':
    app.run(debug=True)
    path: str = RSS_FILE
    summary_rss: str = get_summary_rss(path)
    print(summary_rss)
