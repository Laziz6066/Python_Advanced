"""
Реализуйте приложение для учёта финансов, умеющее запоминать, сколько денег было потрачено за день,
а также показывать затраты за отдельный месяц и за целый год.

В программе должно быть три endpoints:

/add/<date>/<int:number> — сохранение информации о совершённой в рублях трате за какой-то день;
/calculate/<int:year> — получение суммарных трат за указанный год;
/calculate/<int:year>/<int:month> — получение суммарных трат за указанные год и месяц.

Дата для /add/ передаётся в формате YYYYMMDD, где YYYY — год, MM — месяц (от 1 до 12), DD — число (от 01 до 31).
Гарантируется, что переданная дата имеет такой формат и она корректна (никаких 31 февраля).
"""

from flask import Flask
import datetime
import pickle


app = Flask(__name__)

try:
    with open('dates.pickle', 'rb') as f:
        dates = pickle.load(f)
except FileNotFoundError:
    dates = {}


@app.route("/add/<date>/<int:number>")
def add(date: str, number: int):
    try:
        datetime.date.fromisoformat(date)
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")
    year, month, day = map(int, date.split('-'))
    dates.setdefault(year, {}).setdefault(month, {})[day] = number
    return f'Record successfully added.'


@app.route("/calculate/<int:year>")
def calculate_year(year: int):
    total = sum(day[1] for month in dates.get(year, {}).values() for day in month.items())
    return f"Total amount for {year} is {total} rub."


@app.route("/calculate/<int:year>/<int:month>")
def calculate_month(year: int, month: int):
    if year not in dates or month not in dates[year]:
        return "No data available for the given year and month."
    total = sum(dates[year][month].values())
    return f"Total amount for {year}-{month:02d} is {total} rub."


if __name__ == "__main__":
    app.run(debug=True, port=8001)
