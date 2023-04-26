"""
Реализуйте endpoint, начинающийся с /max_number, в который можно передать список чисел, разделённых слешем /.
Endpoint должен вернуть текст «Максимальное переданное число {number}»,
где number — выделенное курсивом наибольшее из переданных чисел.

Примеры:

/max_number/10/2/9/1
Максимальное число: 10

/max_number/1/1/1/1/1/1/1/2
Максимальное число: 2

"""

from flask import Flask

app = Flask(__name__)


@app.route("/max_number/<path:num>")
def max_number(num: str):
    try:
        num_list = [int(x) for x in num.split('/')]
        max_num = max(num_list)
    except ValueError:
        return 'The arguments passed must be numbers!'
    return f'Max number: {max_num}'


if __name__ == "__main__":
    app.run(debug=True, port=8001)
