# FastAPI Weather Service - Debugging Challenge

## Overview

This repository contains a FastAPI weather service that needs to be containerized and deployed to Kubernetes. However, there are several issues throughout the codebase that are preventing it from working correctly.

Your task is to:

1. Write a Dockerfile, and build a docker image for the application
2. Deploy it to a local Kubernetes cluster (minikube)
3. Debug any issues you encounter
4. Fix the problems
5. Successfully deploy a working version of the application
6. Debug the deployment if any issues arise

## Prerequisites

- Docker
- [minikube](https://minikube.sigs.k8s.io/docs/start/?arch=%2Fmacos%2Farm64%2Fstable%2Fbinary+download)
  ```bash
  minikube start
  minikube kubectl # Use this to interact with the cluster, instead of `kubectl`
  ```
- Python 3.8+

## Getting Started

### File Structure

```
fastapi-weather-app/
├── README.md
├── app/
│   ├── main.py
│   ├── weather_data.py
│   └── requirements.txt
├── Dockerfile [missing]
└── kubernetes/
    └── deployment.yaml [with bugs]
```

Clone this repository and examine the code. The application is a simple weather API that provides forecasts for different cities.

### Local Development

```bash
python -m venv venv
source venv/bin/activate
pip install -r app/requirements.txt
export DB_CONNECTION_STRING="postgresql://user:password@localhost:5432/weather_db"
cd app && python main.py
```

#### Test

```bash
curl http://localhost:8000/weather/new%20york
curl http://localhost:8000/health
```

### Building the Docker Image

Write a Dockerfile and build an image:

```bash
docker build -t weather-api:v1 .
```

### Deploying to minikube

1. Start minikube:

```bash
minikube start
```

2. Use minikube's Docker daemon:

```bash
eval $(minikube docker-env)  # On Windows: minikube docker-env | Invoke-Expression
```

3. Build the image in minikube's environment:

```bash
docker build -t weather-api:v1 .
```

4. Deploy to Kubernetes:

```bash
kubectl apply -f kubernetes/deployment.yaml
```

5. Check the deployment:

```bash
kubectl get pods
kubectl get deployments
```

6. Access the application (when it's working):

```bash
minikube service weather-api-service
```

## Debugging Tips

If you encounter issues, check the pod logs:

```bash
kubectl get pods
kubectl logs <pod-name>
```

After fixing issues, rebuild with a new tag and update your deployment as needed.

## Expected Endpoints (when working)

- `GET /`: Welcome message
- `GET /weather/{city}`: Get weather forecast for a specific city
- `GET /health`: Health check endpoint

Good luck!
