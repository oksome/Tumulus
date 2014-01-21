from bottle import Bottle, run
from tumulus.templating import build_template

app = Bottle()


@app.route('/')
def index():
    return build_template('index.tpl.py')


run(app, host='localhost', port=8080)
