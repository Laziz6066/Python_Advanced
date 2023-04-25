import datetime
from flask import Flask

app = Flask(__name__)


@app.route('/test')
def test_function():
    now = datetime.datetime.now().utcnow()
    return f'Это новая тестовая страничка, ответ сгенерирован в {now}'


@app.route('/hello')
def hello():
    return f'Hello world!'


count_value = 0
@app.route('/count')
def count():
    global count_value
    count_value = count_value + 1
    return f'Вы открывали эту страницу {count_value} раз'

