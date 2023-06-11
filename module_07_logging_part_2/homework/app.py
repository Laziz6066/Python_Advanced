import sys, string
import logging
import logging.config
import logging_tree
from utils import string_to_operator
from logging_config import LOGGING_CONFIG


class ASCIIFilter(logging.Filter):
    def is_ascii(self, text):
        return all(ord(char) < 128 for char in text)

    def filter(self, record):
        message = record.getMessage()
        if self.is_ascii(message):
            return True
        return False


def calc(args):
    # Log the arguments
    logger = logging.getLogger('app_log')
    logger.info("Arguments: %s", args)

    num_1 = args[0]
    operator = args[1]
    num_2 = args[2]

    try:
        num_1 = float(num_1)
    except ValueError as e:
        logger.error("Error while converting number 1: %s", e)

    try:
        num_2 = float(num_2)
    except ValueError as e:
        logger.error("Error while converting number 2: %s", e)

    operator_func = string_to_operator(operator)

    result = operator_func(num_1, num_2)

    # Log the result
    logger.info("Result: %s", result)
    logger.info("%s %s %s = %s", num_1, operator, num_2, result)


if __name__ == '__main__':
    calc(sys.argv[1:])

    # Get the logger hierarchy
    tree = logging_tree.format.build_description()

    # Write the result to a file
    with open('logging_tree.txt', 'w') as file:
        file.write(tree)
