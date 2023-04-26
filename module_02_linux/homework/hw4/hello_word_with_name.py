"""
Реализуйте endpoint /hello-world/<имя>, который возвращает строку «Привет, <имя>. Хорошей пятницы!».
Вместо хорошей пятницы endpoint должен уметь желать хорошего дня недели в целом, на русском языке.

Пример запроса, сделанного в субботу:

/hello-world/Саша  →  Привет, Саша. Хорошей субботы!
"""
import sys
from flask import Flask
from datetime import datetime


app = Flask(__name__)


weekdays_tuple = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')


@app.route('/hello-world/<username>')
def hello_world(username):
    weekday = datetime.today().weekday()
    day = weekdays_tuple[weekday]
    return f'Hello, {username}.Have a nice {day}!'


if __name__ == '__main__':
    app.run(debug=True, port=8000)