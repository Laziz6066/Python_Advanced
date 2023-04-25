import datetime
from flask import Flask
import random
import os


app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BOOK_FILE = os.path.join(BASE_DIR, 'war_and_peace.txt')


@app.route('/hello_world')
def hello():
    return 'Hello world'


list_of_cars = ['Chevrolet, Renault, Ford, Lada']
@app.route('/cars')
def cars_list():
    result = ''.join(list_of_cars)
    return f'Список машин: {result}'



cat_breeds = ['корниш-рекс', 'русская голубая', 'шотландская вислоухая', 'мейн-кун', 'манчкин']
@app.route('/cats')
def cats_list():
    return f'Случайная порода кошки: {choice(cat_breeds)}'


@app.route('/get_time/now')
def get_time_now():
    current_time = datetime.datetime.now().utcnow()
    return f'Точное время: {current_time}'


@app.route('/get_time/future')
def get_time_future():
    current_time = datetime.datetime.now().utcnow()
    current_time_after_hour = current_time + datetime.timedelta(hours=1)
    return f'Точное время через час будет: {current_time_after_hour}'


WORDS = []


def load_words():
    global WORDS
    with open("war_and_peace.txt", "r", encoding="utf-8") as f:
        text = f.read().replace('\n', ' ')
        text = ''.join(c for c in text if c not in '.,:;!?()[]{}\'\"')
        WORDS = text.split()


@app.route('/get_random_word')
def random_word():
    if not WORDS:
        load_words()
    word = random.choice(WORDS)
    return f"Случайное слово из книги: {word}"


count_page = 0
@app.route('/counter')
def counter():
    global count_page
    count_page += 1
    return f'Сколько раз открывалась данная страница: {count_page}'


if __name__ == '__main__':
    app.run(debug=True)
