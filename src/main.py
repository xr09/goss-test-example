from flask import Flask, redirect
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, All!'

@app.route('/hi/<name>')
def hi(name):
    return 'Hi, {}!'.format(name)

@app.route('/redir')
def other():
    return redirect('https://example.org', code=302)
