import logging
import requests


class FlaskHandler(logging.Handler):
    def __init__(self, url):
        super().__init__()
        self.url = url

    def emit(self, record):
        log_data = self.format(record)
        headers = {'Content-Type': 'application/json'}
        response = requests.post(self.url, json=log_data, headers=headers)
        if response.status_code != 200:
            print('Failed to send log:', response.text)
