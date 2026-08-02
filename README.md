# End-to-End MLOps Capstone Project with AWS, Docker, Kubernetes, DVC & MLflow

## Overview

This project demonstrates a complete **production-grade MLOps pipeline** for a Machine Learning application. It covers the entire lifecycle from data ingestion and experimentation to model deployment on Kubernetes with automated CI/CD and monitoring.

The project integrates modern MLOps tools including:

* MLflow
* DVC
* DagsHub
* Docker
* GitHub Actions
* AWS S3
* Amazon ECR
* Amazon EKS
* Prometheus
* Grafana
* Flask

The goal is to build an automated, reproducible, scalable, and cloud-native machine learning system.

---

# Architecture

```
                   GitHub Repository
                          │
                          ▼
                 GitHub Actions (CI/CD)
                          │
          ┌───────────────┴───────────────┐
          │                               │
          ▼                               ▼
      Run Tests                     Build Docker Image
          │                               │
          ▼                               ▼
     Register Model                 Push Image to ECR
          │                               │
          └───────────────┬───────────────┘
                          ▼
                 Deploy to Amazon EKS
                          │
                          ▼
                     Flask API
                          │
                          ▼
                  ML Model Prediction
                          │
        ┌─────────────────┴─────────────────┐
        ▼                                   ▼
   Prometheus                        Grafana Dashboard

```

---

# Tech Stack

| Category            | Technologies            |
| ------------------- | ----------------------- |
| Language            | Python 3.10             |
| Version Control     | Git, GitHub             |
| Experiment Tracking | MLflow, DagsHub         |
| Data Versioning     | DVC                     |
| Model Storage       | AWS S3                  |
| Cloud Platform      | AWS                     |
| Containerization    | Docker                  |
| Container Registry  | Amazon ECR              |
| Orchestration       | Kubernetes (Amazon EKS) |
| CI/CD               | GitHub Actions          |
| Monitoring          | Prometheus              |
| Visualization       | Grafana                 |
| Web Framework       | Flask                   |

---

# Project Structure

```
.
├── data
│   ├── raw
│   ├── interim
│   └── processed
│
├── notebooks
│
├── src
│   ├── logger
│   ├── data
│   │     ├── data_ingestion.py
│   │     ├── data_preprocessing.py
│   │     ├── feature_engineering.py
│   │
│   ├── model
│   │     ├── model_building.py
│   │     ├── model_evaluation.py
│   │     └── register_model.py
│
├── flask_app
│
├── tests
│
├── scripts
│
├── .github
│   └── workflows
│       └── ci.yaml
│
├── params.yaml
├── dvc.yaml
├── Dockerfile
├── requirements.txt
└── README.md
```

---

# Features

* End-to-End ML Pipeline
* Data Versioning using DVC
* Experiment Tracking using MLflow
* Remote Experiment Tracking on DagsHub
* Model Registration
* Dockerized Flask API
* CI/CD using GitHub Actions
* AWS S3 Artifact Storage
* Amazon ECR Image Registry
* Kubernetes Deployment on Amazon EKS
* Monitoring with Prometheus
* Dashboards using Grafana

---

# Workflow

## 1. Project Setup

* Create GitHub repository
* Create Conda environment
* Generate project using Cookiecutter
* Initialize Git

---

## 2. Experiment Tracking

MLflow is configured with DagsHub for:

* Parameter logging
* Metrics logging
* Artifact logging
* Model Registry

---

## 3. Data Versioning

DVC is used to:

* Version datasets
* Build reproducible pipelines
* Store artifacts in AWS S3

Pipeline stages include:

* Data Ingestion
* Data Preprocessing
* Feature Engineering
* Model Training
* Model Evaluation

---

## 4. Model Training

Training pipeline includes:

* Data cleaning
* Feature engineering
* Model training
* Hyperparameter tuning
* Evaluation
* Model registration

---

## 5. Flask API

The trained model is served through a Flask REST API.

Example endpoint:

```
POST /predict
```

Returns predictions as JSON.

---

## 6. Dockerization

The Flask application is packaged into a Docker image.

```
docker build -t capstone-app:latest .
```

Run locally

```
docker run -p 8888:5000 \
-e CAPSTONE_TEST=<YOUR_TOKEN> \
capstone-app:latest
```

---

## 7. CI Pipeline

GitHub Actions automatically performs:

* Install dependencies
* Run tests
* Execute validation scripts
* Build Docker image
* Push image to Amazon ECR

---

## 8. CD Pipeline

After a successful CI build:

* Pull latest Docker image
* Deploy to Amazon EKS
* Update Kubernetes deployment

---

## 9. Monitoring

Prometheus continuously scrapes metrics from the Flask application.

Grafana connects to Prometheus and provides dashboards for:

* Request count
* Response latency
* Error rate
* System metrics

---

# DVC Pipeline

```
Data Ingestion
        │
        ▼
Data Preprocessing
        │
        ▼
Feature Engineering
        │
        ▼
Model Training
        │
        ▼
Model Evaluation
        │
        ▼
Model Registration
```

Run pipeline

```
dvc repro
```

Check status

```
dvc status
```

Push artifacts

```
dvc push
```

---

# AWS Services Used

* Amazon S3
* Amazon ECR
* Amazon EKS
* IAM
* EC2
* CloudFormation
* Security Groups

---

# Kubernetes Deployment

Deployments include

* Flask Deployment
* LoadBalancer Service
* Secrets
* Configurations

Useful commands

```
kubectl get pods

kubectl get svc

kubectl get deployments

kubectl get nodes
```

---

# Monitoring Stack

### Prometheus

Responsible for

* Metric collection
* Application scraping
* Performance monitoring

Runs on

```
http://<EC2-IP>:9090
```

---

### Grafana

Responsible for

* Dashboard visualization
* Real-time monitoring
* Alerting

Runs on

```
http://<EC2-IP>:3000
```

Default credentials

```
Username: admin

Password: admin
```

---

# GitHub Secrets

The following secrets are required.

```
CAPSTONE_TEST

AWS_ACCESS_KEY_ID

AWS_SECRET_ACCESS_KEY

AWS_REGION

AWS_ACCOUNT_ID

ECR_REPOSITORY
```

---

# Local Setup

Clone repository

```bash
git clone <repository-url>

cd <repository>
```

Create environment

```bash
conda create -n atlas python=3.10

conda activate atlas
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run pipeline

```bash
dvc repro
```

Run Flask application

```bash
python app.py
```

---

# CI/CD Flow

```
Developer

      │

      ▼

Push to GitHub

      │

      ▼

GitHub Actions

      │

      ▼

Run Tests

      │

      ▼

Train Model

      │

      ▼

Register Model

      │

      ▼

Build Docker Image

      │

      ▼

Push to Amazon ECR

      │

      ▼

Deploy to Amazon EKS

      │

      ▼

Application Live

      │

      ▼

Prometheus

      │

      ▼

Grafana Dashboard
```

---

# Cloud Infrastructure

```
GitHub
   │
   ▼
GitHub Actions
   │
   ▼
Amazon ECR
   │
   ▼
Amazon EKS
   │
   ▼
Flask Application
   │
   ▼
ML Model

S3
│
└── DVC Storage

Prometheus
      │
      ▼
Grafana
```

---

# Future Improvements

* Terraform Infrastructure as Code
* Helm Charts for Kubernetes
* Canary Deployments
* Blue-Green Deployments
* Auto Scaling (HPA)
* ArgoCD GitOps Deployment
* Model Drift Detection
* Data Drift Monitoring
* Feature Store Integration
* Automated Retraining Pipeline
* Slack/Email Alerting
* Unit, Integration, and Performance Testing

---

# Learning Outcomes

This project demonstrates practical experience with:

* Production MLOps workflows
* Experiment tracking
* Data versioning
* Docker containerization
* Kubernetes deployment
* AWS cloud services
* CI/CD automation
* Monitoring and observability
* Model lifecycle management
* Reproducible machine learning pipelines

---

# Acknowledgements

This project was built to gain hands-on experience with modern MLOps practices by integrating industry-standard open-source tools and AWS cloud services into a complete machine learning deployment workflow.