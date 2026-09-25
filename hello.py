from flask import Flask

app = Flask(__name__)


@app.route('/')
def say_hello():
    return ('<p>Welcome! This is another string!</p>'
            '<p><a href="/about">About this app</a></p>'
            '<p><a href="/contact">Contact</a></p>')


@app.route('/about')
def about():
    return ('<p>This application is running on the Flask web framework.</p>'
            '<p>Learn more about Flask: <a href="https://flask.palletsprojects.com/">https://flask.palletsprojects.com/</a></p>'
            '<p>Learn more about Python: <a href=https://www.python.org/">https://www.python.org/</a></p>'
            '<p><a href="/">Back to home</a></p>')


@app.route('/contact')
def contact():
    return ('<p>Contact me at: <a href="mailto:r19mahi@gmail.com">r19mahi@gmail.com</a></p>'
            '<p><a href="/">Back to home</a></p>')