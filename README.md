# devops-flask-app

Intro to DevOps - a minimal Flask web app used for the labs.

| File | What it is |
|------|------------|
| `hello.py` | The Flask app (routes: `/`, `/about`, `/contact`) |
| `Dockerfile` | Lab 5: builds a container image that serves the app on port 5000 |
| `requirements.txt` | Python packages the app needs (Flask) |
| `setup.sh` | Lab 1 script: installs packages on Ubuntu Server, creates a venv, installs Flask and runs the app |

## Run it

```
python -m venv .my_venv
source .my_venv/bin/activate
pip install flask
flask --app hello run --host=0.0.0.0
```

Then open http://localhost:5000

## Run it with Docker

```
docker buildx build -t my_flask_image .
docker run -p 8080:5000 --name my_flask_container my_flask_image
```

Then open http://localhost:8080
