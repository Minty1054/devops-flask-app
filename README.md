# devops-flask-app

Intro to DevOps - a minimal Flask web app used for the labs.

| File | What it is |
|------|------------|
| `hello.py` | The Flask app (routes: `/`, `/about`, `/contact`) |
| `setup.sh` | Lab 1 script: installs packages on Ubuntu Server, creates a venv, installs Flask and runs the app |

## Run it

```
python -m venv .my_venv
source .my_venv/bin/activate
pip install flask
flask --app hello run --host=0.0.0.0
```

Then open http://localhost:5000