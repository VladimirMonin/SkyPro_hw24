import os

from flask import Flask, request, abort

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


@app.route("/perform_query", methods=['POST', 'GET'])
def perform_query():
    cmd1 = request.args.get('cmd1')
    val1 = request.args.get('val1')
    file_name = request.args.get('file_name')

    if not (cmd1 or val1 or file_name):
        abort(400)

    file_path = os.path.join(DATA_DIR, file_name)
    if not os.path.exists(file_path):
        return abort(400, 'File not found')

    # получить параметры query и file_name из request.args, при ошибке вернуть ошибку 400
    # проверить, что файла file_name существует в папке DATA_DIR, при ошибке вернуть ошибку 400
    # с помощью функционального программирования (функций filter, map), итераторов/генераторов сконструировать запрос
    # вернуть пользователю сформированный результат
    return app.response_class('', content_type="text/plain")

if __name__ == '__main__':
    app.run(debug=True)
