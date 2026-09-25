#!/bin/bash
# Lab 1 - automatically install and run the Flask app on Ubuntu Server 24.04.
# Runs with no user input: -y answers "yes" to apt, and
# DEBIAN_FRONTEND=noninteractive stops packages (e.g. tzdata) asking questions.
set -e

# Use sudo on a normal VM user; skip it when already root (e.g. Docker container)
if [ "$(id -u)" -ne 0 ]; then SUDO=sudo; else SUDO=; fi

# 1. Update and upgrade the system
$SUDO apt-get update
$SUDO env DEBIAN_FRONTEND=noninteractive apt-get -y dist-upgrade

# 2. Install the required apt packages
$SUDO env DEBIAN_FRONTEND=noninteractive apt-get -y install \
    nano vim python-is-python3 python3-venv python3-pip

# 3. Create and activate a virtual environment
APP_DIR="$HOME/flask_app"
mkdir -p "$APP_DIR"
cd "$APP_DIR"
python -m venv .my_venv
source .my_venv/bin/activate

# 4. Install Flask into the venv
pip install flask

# 5. Write the Flask app
cat > hello.py <<'EOF'
from flask import Flask

app = Flask(__name__)


@app.route('/')
def say_hello():
    return '<p>Hello, World, I am a Flask app!</p><p><a href="/about">About this app</a></p>'


@app.route('/about')
def about():
    return ('<p>This application is running on the Flask web framework.</p>'
            '<p>Learn more about Flask: <a href="https://flask.palletsprojects.com/">https://flask.palletsprojects.com/</a></p>'
            '<p><a href="/">Back to home</a></p>')
EOF

# 6. Start the Flask development server on port 5000, reachable from the host
flask --app hello run --host=0.0.0.0
