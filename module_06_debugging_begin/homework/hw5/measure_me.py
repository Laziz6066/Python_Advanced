"""
Каждый лог содержит в себе метку времени, а значит, правильно организовав логирование,
можно отследить, сколько времени выполняется функция.

Программа, которую вы видите, по умолчанию пишет логи в stdout. Внутри неё есть функция measure_me,
в начале и в конце которой пишется "Enter measure_me" и "Leave measure_me".
Сконфигурируйте логгер, запустите программу, соберите логи и посчитайте среднее время выполнения функции measure_me.
"""
import logging
import random
from typing import List
import re
from datetime import datetime


logger = logging.getLogger(__name__)


def get_data_line(sz: int) -> List[int]:
    try:
        logger.debug("Enter get_data_line")
        return [random.randint(-(2 ** 31), 2 ** 31 - 1) for _ in range(sz)]
    finally:
        logger.debug("Leave get_data_line")


def measure_me(nums: List[int]) -> List[List[int]]:
    logger.debug("Enter measure_me")
    results = []
    nums.sort()

    for i in range(len(nums) - 2):
        logger.debug(f"Iteration {i}")
        left = i + 1
        right = len(nums) - 1
        target = 0 - nums[i]
        if i == 0 or nums[i] != nums[i - 1]:
            while left < right:
                s = nums[left] + nums[right]
                if s == target:
                    logger.debug(f"Found {target}")
                    results.append([nums[i], nums[left], nums[right]])
                    logger.debug(
                        f"Appended {[nums[i], nums[left], nums[right]]} to result"
                    )
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif s < target:
                    logger.debug(f"Increment left (left, right) = {left, right}")
                    left += 1
                else:
                    logger.debug(f"Decrement right (left, right) = {left, right}")

                    right -= 1

    logger.debug("Leave measure_me")

    return results


def calculate_average_execution_time(log_file):
    start_times = []
    execution_times = []

    with open(log_file, 'r') as file:
        lines = file.readlines()

    for line in lines:
        if 'Enter measure_me' in line:
            start_time = re.search(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}', line)
            if start_time:
                start_times.append(datetime.strptime(start_time.group(), '%Y-%m-%d %H:%M:%S,%f'))
        elif 'Leave measure_me' in line:
            end_time = re.search(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}', line)
            if end_time:
                end_time = datetime.strptime(end_time.group(), '%Y-%m-%d %H:%M:%S,%f')
                execution_times.append((end_time - start_times.pop()).total_seconds() * 1000)

    average_execution_time = sum(execution_times) / len(execution_times)
    return average_execution_time


if __name__ == "__main__":
    logging.basicConfig(level="DEBUG", filename='log.txt',
                        format=('%(asctime)s - %(levelname)s - %(message)s'))
    for it in range(15):
        data_line = get_data_line(10 ** 3)
        measure_me(data_line)

    average_time = calculate_average_execution_time('log.txt')
    print(f'Average execution time: {average_time} ms')

