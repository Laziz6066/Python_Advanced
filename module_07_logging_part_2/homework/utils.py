import logging
from typing import Union, Callable
from operator import sub, mul, truediv, add
from logging.handlers import TimedRotatingFileHandler

OPERATORS = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': truediv,
}

Numeric = Union[int, float]


def configure_logging() -> None:
    """
    Configure logging using basicConfig and apply formatting to all handlers.
    """
    # Create a logger for the utils module
    logger = logging.getLogger('utils')
    logger.setLevel(logging.INFO)

    # Create a TimedRotatingFileHandler
    file_handler = TimedRotatingFileHandler('utils.log', when='H', interval=1, backupCount=10)
    file_handler.setLevel(logging.INFO)

    # Set the log format
    formatter = logging.Formatter('%(levelname)s | %(name)s | %(asctime)s | %(lineno)d | %(message)s')
    file_handler.setFormatter(formatter)

    # Add the file handler to the logger
    logger.addHandler(file_handler)

def string_to_operator(value: str) -> Callable[[Numeric, Numeric], Numeric]:
    """
    Convert string to arithmetic function
    :param value: basic arithmetic function
    """
    if not isinstance(value, str):
        logging.error("Wrong operator type: %s", value)
        raise ValueError("Wrong operator type")

    if value not in OPERATORS:
        logging.error("Wrong operator value: %s", value)
        raise ValueError("Wrong operator value")

    return OPERATORS[value]


# Configure logging
configure_logging()

# Rest of the code...
