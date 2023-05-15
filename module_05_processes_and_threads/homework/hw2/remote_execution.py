"""
Напишите эндпоинт, который принимает на вход код на Python (строка)
и тайм-аут в секундах (положительное число не больше 30).
Пользователю возвращается результат работы программы, а если время, отведённое на выполнение кода, истекло,
то процесс завершается, после чего отправляется сообщение о том, что исполнение кода не уложилось в данное время.
"""

from flask import Flask, jsonify, request
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators
import subprocess

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'


class CodeForm(FlaskForm):
    code = StringField('Code', [validators.InputRequired()])
    timeout = IntegerField('Timeout', [validators.InputRequired(), validators.NumberRange(min=1, max=30)])


def run_python_code_in_subprocess(code: str, timeout: int):
    p = subprocess.Popen(["python", "-c", code], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    try:
        out, err = p.communicate(timeout=timeout)
        return out.decode() + err.decode()
    except subprocess.TimeoutExpired:
        p.kill()
        return "Code execution timed out"


@app.route('/run_code', methods=['POST'])
def run_code():
    form = CodeForm(request.form)
    if form.validate():
        code = form.code.data
        timeout = form.timeout.data
        output = run_python_code_in_subprocess(code, timeout)
        return jsonify({"output": output})
    else:
        return jsonify({"error": "Invalid input"}), 400


if __name__ == '__main__':
    app.run(debug=True)
