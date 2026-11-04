# devops-flask-app

Intro to DevOps - a minimal Flask web app used for the labs.

| File | What it is |
|------|------------|
| `hello.py` | The Flask app (routes: `/`, `/about`, `/contact`) |
| `Dockerfile` | Lab 5: builds a container image that serves the app on port 5000 |
| `requirements.txt` | Python packages the app needs (Flask, Redis) |
| `compose.yaml` | Lab 6: runs the Flask app and a Redis cache in separate containers |
| `redis-server-deployment.yaml` | Lab 7: Kubernetes deployment for Redis |
| `redis-service.yaml` | Lab 7: ClusterIP service so the app can reach Redis at `the-redis-server` |
| `flask-app-deployment.yaml` | Lab 7: Kubernetes deployment running 5 replicas of the Flask app |
| `load-balancer.yaml` | Lab 7: LoadBalancer service exposing the app on port 80 |
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

## Run it with Docker Compose (Lab 6)

Each route caches its HTML in Redis for 10 minutes.

```
docker compose up --build
```

Then open http://localhost:8080

## Run it on Kubernetes (Lab 7)

```
minikube start
eval $(minikube -p minikube docker-env)
docker build -t my_flask_image .
kubectl create -f redis-server-deployment.yaml
kubectl create -f redis-service.yaml
kubectl create -f flask-app-deployment.yaml
kubectl create -f load-balancer.yaml
minikube tunnel        # in a second terminal
kubectl get svc        # use the EXTERNAL-IP of flaskapp-service
```
