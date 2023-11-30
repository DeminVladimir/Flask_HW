from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/wallet')
def wallet():
    return render_template('wallet.html')


@app.route('/belts')
def belts():
    return render_template('belts.html')


@app.route('/tools')
def tools():
    return render_template('tools.html')


@app.route('/contacts')
def contacts():
    return render_template('contacts.html')


if __name__ == '__main__':
    app.run()
