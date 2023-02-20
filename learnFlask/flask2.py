from flask import Flask
from flask import request, session

app = Flask(__name__)

@app.route('/')
def index():
    text = 'This is a website!'
    text += '\n<p><a href = "/hello">Hello</a>'
    return text

@app.route('/hello')
def hello():
    return f'Hello anonymous person.'

@app.route('/hello/<name>')
def greet(name):
    return f'Hello there, {name}'

@app.route('/request_view')
def request_view():
    response_text = ''
    response_text += '<h1>Headers</h1>'
    for key, value in request.headers:
        response_text += f'<p>{key}: {value}'

    response_text += '<h1>Args</h1>'
    for value in request.args:
        response_text += f'<p>{value}: {request.args.get(value)}'

    response_text += '<h1>Path</h1>'
    response_text += f'<p>{request.path}'

    response_text += '<h1>URL</h1>'
    response_text += f'<p>{request.url}'

    return response_text

@app.route('/add')
def add():
    first_number = request.args.get('first', '')
    second_number = request.args.get('second', '')
    if first_number and second_number:
        try:
            result = int(first_number) + int(second_number)
        except ValueError:
            return 'Invalid data'
        return f'{first_number} + {second_number} = {result}'
    else:
        return 'No arguments detected'


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)