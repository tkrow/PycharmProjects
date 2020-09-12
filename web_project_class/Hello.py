from flask import Flask

app = Flask(__name__)


@app.route('/hello/<name>')  # route decorator
def hello_name(name):
    return 'Hello %s!' % name
app.add_url_rule('/', 'hello', hello_name)

@app.route('/flask')
def hello_flask():
    return 'Hello Flask'

@app.route('/capstone')
def hello_capstone():
    return 'This is a capstone'

if __name__ == '__main__':
    app.run(debug=True)
