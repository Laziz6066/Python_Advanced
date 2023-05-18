"""
Ваш коллега, применив JsonAdapter из предыдущей задачи, сохранил логи работы его сайта за сутки
в файле skillbox_json_messages.log. Помогите ему собрать следующие данные:

1. Сколько было сообщений каждого уровня за сутки.
2. В какой час было больше всего логов.
3. Сколько логов уровня CRITICAL было в период с 05:00:00 по 05:20:00.
4. Сколько сообщений содержит слово dog.
5. Какое слово чаще всего встречалось в сообщениях уровня WARNING.
"""
from typing import Dict
import json
from datetime import datetime
from collections import Counter
import re


def task1() -> Dict[str, int]:
    """
    1. Сколько было сообщений каждого уровня за сутки.
    @return: словарь вида {уровень: количество}
    """
    info, debug, critical, warning, error = 0, 0, 0, 0, 0

    with open('skillbox_json_messages.log', 'r', encoding='utf-8') as file:
        for line in file:
            data = json.loads(line)
            if data['level'] == 'INFO': info += 1
            elif data['level'] == 'DEBUG': debug += 1
            elif data['level'] == 'CRITICAL': critical += 1
            elif data['level'] == 'WARNING': warning += 1
            elif data['level'] == 'ERROR': error += 1

    return f'\nINFO: {info}\nDEBUG: {debug}\nCRITICAL: {critical}\nWARNING: {warning}\nERROR: {error}'


def task2() -> int:
    """
    2. В какой час было больше всего логов.
    @return: час
    """
    hour_counter = Counter()

    with open('skillbox_json_messages.log', 'r', encoding='utf-8') as file:
        for line in file:
            try:
                data = json.loads(line)
                timestamp = datetime.strptime(data["time"], "%H:%M:%S")
                hour = timestamp.hour
                hour_counter[hour] += 1
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {str(e)}")

    most_common_hour = hour_counter.most_common(1)

    hour, count = most_common_hour[0]
    return f"С {hour}:00 по {hour}:59 было больше всего логов. Кол-во: {count}"


def task3() -> int:
    """
    3. Сколько логов уровня CRITICAL было в период с 05:00:00 по 05:20:00.
    @return: количество логов
    """
    count = 0

    start_time = datetime.strptime('05:00:00', "%H:%M:%S")
    end_time = datetime.strptime('05:20:00', "%H:%M:%S")

    with open('skillbox_json_messages.log', 'r', encoding='utf-8') as file:
        for line in file:
            data = json.loads(line)
            if data['level'] == 'CRITICAL':
                timestamp = datetime.strptime(data["time"], "%H:%M:%S")
                if start_time <= timestamp <= end_time:
                    count += 1

    return f'Кол-во логов уровня CRITICAL: {count}'


def task4() -> int:
    """
    4. Сколько сообщений содержат слово dog.
    @return: количество сообщений
    """

    count = 0

    with open('skillbox_json_messages.log', 'r', encoding='utf-8') as file:
        for line in file:
            data = json.loads(line)
            if 'dog' in data['message']:
                count += 1

    return f'"{count}" -- сообщений содержат слово dog'


def task5() -> str:
    """
    5. Какое слово чаще всего встречалось в сообщениях уровня WARNING.
    @return: слово
    """
    word_counter = Counter()

    with open('skillbox_json_messages.log', 'r', encoding='utf-8') as file:
        for line in file:
            data = json.loads(line)
            if "level" in data and data["level"] == "WARNING":
                message = data["message"]
                words = re.findall(r"\w+(?:'\w+)?", message.lower())
                word_counter.update(words)

    most_common_word = word_counter.most_common(1)

    return f'Слово: [ {most_common_word[0][0]} ] чаще всего встречалось в сообщениях уровня WARNING'


if __name__ == '__main__':
    tasks = (task1, task2, task3, task4, task5)
    for i, task_fun in enumerate(tasks, 1):
        task_answer = task_fun()
        print(f'{i}. {task_answer}')
