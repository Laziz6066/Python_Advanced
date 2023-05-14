"""
Напишите GET-эндпоинт /ps, который принимает на вход аргументы командной строки,
а возвращает результат работы команды ps с этими аргументами.
Входные значения эндпоинт должен принимать в виде списка через аргумент arg.

Например, для исполнения команды ps aux запрос будет следующим:

/ps?arg=a&arg=u&arg=x
"""

from flask import Flask, request
import shlex, subprocess

app = Flask(__name__)


@app.route("/ps", methods=["GET"])
def ps() -> str:
    args = request.args.getlist('arg')
    cmd = ['ps'] + args
    clean_cmd = [shlex.quote(arg) for arg in cmd]
    result = subprocess.check_output(clean_cmd).decode('utf-8')
    formatted_result = f'<pre>{result}</pre>'
    return formatted_result


if __name__ == "__main__":
    app.run(debug=True)
