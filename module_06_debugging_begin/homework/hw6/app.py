"""
Заменим сообщение "The requested URL was not found on the server" на что-то более информативное.
Например, выведем список всех доступных страниц с возможностью перехода по ним.

Создайте Flask Error Handler, который при отсутствии запрашиваемой страницы будет выводить
список всех доступных страниц на сайте с возможностью перехода на них.
"""

from flask import Flask, render_template
from werkzeug.routing import Rule

app = Flask(__name__)


def get_available_pages():
    rules = app.url_map.iter_rules()
    available_pages = []
    for rule in rules:
        if not isinstance(rule, Rule) or rule.endpoint == 'static':
            continue
        available_pages.append(rule.rule)
    return available_pages


def render_available_pages():
    available_pages = get_available_pages()
    return render_template('available_pages.html', pages=available_pages)


@app.errorhandler(404)
def page_not_found(e):
    return render_available_pages(), 404


@app.route('/dogs')
def dogs():
    return 'Страница с пёсиками'


@app.route('/cats')
def cats():
    return 'Страница с котиками'


@app.route('/cats/<int:cat_id>')
def cat_page(cat_id: int):
    return f'Страница с котиком {cat_id}'


@app.route('/index')
def index():
    return 'Главная страница'


if __name__ == '__main__':
    app.run(debug=True)
