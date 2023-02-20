from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'This is a website!'

@app.route('/hello')
def hello():
    return 'Hello Anonymous person'

@app.route('/hello/<name>')
def greet(name):
    return f'Hello There, {name}'

if __name__  == '__main__':
    app.run(host = "127.0.0.1", port = 80, debug = True)