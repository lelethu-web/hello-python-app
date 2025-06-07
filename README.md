# Hello Python App 🚀

A simple Hello World Python application deployed using Docker, Kubernetes, and Helm.

---

## 🧰 Project Structure

hello-python-app/
├── app/ # Python Flask Hello World app
│ └── app.py
├── Dockerfile # Container build file
├── hello-python/ # Helm chart for deployment
│ ├── Chart.yaml
│ ├── values.yaml
│ └── templates/
│ ├── deployment.yaml
│ ├── service.yaml
│ └── ...
└── README.md


## 🚀 Argo CD Setup

Login to Argo CD:

```bash
argocd login localhost:8084 --username admin --password <your-password> --insecure

