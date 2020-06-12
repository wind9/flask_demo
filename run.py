from flask import Flask
import os


demo = os.environ['demo']
app = Flask(__name__)


@app.route('/')
def index():
    return 'hello {}'.format(demo)


@app.route('/test')
def index2():
    return 'hello {} in dir /test'.format(demo)


@app.route('/test2')
def index3():
    return 'hello {} in dir /test2'.format(demo)


app.run(host='localhost', port='8080')
