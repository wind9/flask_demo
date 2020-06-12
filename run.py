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
def index2():
    return 'hello {} in dir /test2'.format(demo)


print(demo)
app.run(host='127.0.0.1', port='8080')
