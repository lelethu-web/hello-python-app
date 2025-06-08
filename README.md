******Hello Python App – Kubernetes GitOps Workflow

A simple Python web app deployed using Kubernetes, Docker, Helm, GitHub Actions, and Argo CD******

.Project Structure


├── app.py                      # Simple Python app (Flask)
├── Dockerfile                 # Docker build config
├── requirements.txt           # Python dependencies
├── values.yaml                # Helm values
├── Chart.yaml                 # Helm chart metadata
├── templates/                 # Helm templates
│   ├── deployment.yaml
│   ├── service.yaml
│   └── NOTES.txt
├── .github/
    └── workflows/
        └── docker-build-push.yml  # GitHub Actions CI
        
**What This Does**

Build & push Docker images to Docker Hub on git push.

Deploy the app to a local Kubernetes cluster via Helm.

Use Argo CD to watch the Git repo and sync deployments automatically.


**Prerequisites**

Docker

kind (Kubernetes in Docker)

kubectl

Helm

Argo CD installed in your cluster

GitHub Actions configured with secrets:

DOCKERHUB_USERNAME

DOCKERHUB_TOKEN

 **Docker**

docker build -t hello-python .
docker run -p 5000:5000 hello-python

 Deploying to Kubernetes (locally with kind)


 kind create cluster --name hello-python
 helm install hello-python .  # assumes you're in the chart directory
 kubectl get svc hello-python-service
 kubectl get nodes -o wide


** **GitHub Actions CI (Docker Build + Push)**

.github/workflows/docker-build-push.yml:**



name: Build and Push Docker Image

on:
  push:
    branches:
      - main

jobs:
  build-and-push:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: docker/setup-buildx-action@v3

      - uses: docker/login-action@v3
        with:
          username: ${{ secrets.DOCKERHUB_USERNAME }}
          password: ${{ secrets.DOCKERHUB_TOKEN }}

      - uses: docker/build-push-action@v5
        with:
          context: .
          file: ./Dockerfile
          push: true
          tags: b37775b30994/hello-python:latest

         ** Every push to main triggers this workflow, builds a Docker image, and pushes it to Docker Hub**


         **Argo CD Setup**

kubectl create namespace argocd

kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

kubectl port-forward svc/argocd-server -n argocd 8081:443

argocd app create hello-python-app \
  --repo https://github.com/lelethu-web/hello-python-app.git \
  --path . \
  --dest-server https://kubernetes.default.svc \
  --dest-namespace default \
  --sync-policy automated


Watch Argo CD Sync Automatically

Now when you push changes (Dockerfile, manifests, Helm values), GitHub Actions will:

Build & push new Docker image.

Argo CD will detect the Helm chart update and re-deploy automatically
