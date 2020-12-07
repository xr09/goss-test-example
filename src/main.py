from flask import Flask, redirect
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/hi/<name>')
def hi(name):
    return 'Hey, {}!'.format(name)

@app.route('/redir')
def other():
    return redirect('https://example.org', code=302)
