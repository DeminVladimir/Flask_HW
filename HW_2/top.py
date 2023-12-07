# Задание
# Создать страницу, на которой будет форма для ввода имени и электронной почты, при отправке которой будет создан
# cookie-файл с данными пользователя, а также будет произведено перенаправление на страницу приветствия,
# где будет отображаться имя пользователя.
# На странице приветствия должна быть кнопка «Выйти», при нажатии на которую будет удалён cookie-файл с данными
# пользователя и произведено перенаправление на страницу ввода имени и электронной почты.


from flask import Flask, url_for
from flask import render_template
from flask import request
from flask import make_response
from flask import redirect

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        res = make_response(redirect(url_for('hello', name=name, email=email)))
        res.set_cookie('name', name)
        res.set_cookie('email', email)
        return res
    return render_template('index.html')


@app.route('/hello/<string:name>/<string:email>', methods=['GET', 'POST'])
def hello(name, email):
    if request.method == 'POST':
        res = make_response(redirect(url_for('index')))
        res.set_cookie('name', name, max_age=0)
        res.set_cookie('email', email, max_age=0)
        return res
    return render_template('hello.html', name=name)


if __name__ == '__main__':
    app.run()
