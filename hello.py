import json
import os
import time

import redis
from flask import Flask

app = Flask(__name__)

# Redis runs in its own container. The hostname is the Compose service name
# ("redis-server"); on Kubernetes it is overridden with the REDIS_HOST env var.
r = redis.Redis(host=os.environ.get('REDIS_HOST', 'redis-server'),
                port=6379, decode_responses=True)

# 600 seconds == 10 minutes
CACHE_SECONDS = 600


@app.route('/')
def say_hello():
    data = r.get('home')
    if data is not None:
        data = json.loads(data)
        if time.time() - data['time'] <= CACHE_SECONDS:
            return data['html']

    data = ('<p>Welcome! This is another string!</p>'
            '<p><a href="/about">About this app</a></p>'
            '<p><a href="/contact">Contact</a></p>')
    r.set('home', json.dumps({
        'html': data,
        'time': time.time()
    }))
    return data


@app.route('/about')
def about():
    data = r.get('about')
    if data is not None:
        data = json.loads(data)
        if time.time() - data['time'] <= CACHE_SECONDS:
            return data['html']

    data = ('<p>This application is running on the Flask web framework.</p>'
            '<p>Learn more about Flask: <a href="https://flask.palletsprojects.com/">https://flask.palletsprojects.com/</a></p>'
            '<p>Learn more about Python: <a href="https://www.python.org/">https://www.python.org/</a></p>'
            '<p><a href="/">Back to home</a></p>')
    r.set('about', json.dumps({
        'html': data,
        'time': time.time()
    }))
    return data


@app.route('/contact')
def contact():
    data = r.get('contact')
    if data is not None:
        data = json.loads(data)
        if time.time() - data['time'] <= CACHE_SECONDS:
            return data['html']

    data = ('<p>Contact me at: <a href="mailto:r19mahi@gmail.com">r19mahi@gmail.com</a></p>'
            '<p><a href="/">Back to home</a></p>')
    r.set('contact', json.dumps({
        'html': data,
        'time': time.time()
    }))
    return data
