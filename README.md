MLOps Pipeline: FastAPI + AWS + CI/CD
Adrian Charbonneau
Overview

This project demonstrates an end-to-end MLOps pipeline:

    Train a simple ML model using linear regression with Iris dataset.

    Serve predictions via FastAPI.

    Containerize using Docker.

    Automate CI/CD with GitHub Actions.

    Set up testing with test_app.py and pytest.

    Deploy on AWS (Lambda or ECS Fargate).

Project Architecture:

    Lambda Deployment:
    ┌────────────┐       ┌─────────────┐       ┌─────────────┐
    │   GitHub   │ ----> │    ECR      │ ----> │   Lambda    │
    │ Actions CI │       │  (Image)    │       │ (Container) │
    └────────────┘       └─────────────┘       └─────────────┘
                                                │
                                                v
                                        ┌─────────────┐
                                        │ API Gateway │
                                        └─────────────┘
                                                │
                                                v
                                            End Users


    ECS Deployment:
    ┌────────────┐       ┌─────────────┐       ┌─────────────┐
    │   GitHub   │ ----> │    ECR      │ ----> │ ECS Fargate │
    │ Actions CI │       │  (Image)    │       │  (Service)  │
    └────────────┘       └─────────────┘       └─────────────┘
                                                │
                                                v
                                        ┌─────────────┐
                                        │   ALB       │
                                        │ (Load Bal.) │
                                        └─────────────┘
                                                │
                                                v
                                            End Users


Tech Stack:

    Language: Python 3.10

    Framework: FastAPI

    ML Library: scikit-learn

    Containerization: Docker

    CI/CD: GitHub Actions

    Cloud: AWS (Lambda, ECS, ECR, API Gateway, ALB)

    IaC (optional): Terraform

Features

    Model training (train.py)
    REST API (FastAPI with Swagger UI)
    Dockerized application
    Automated testing with pytest
    CI/CD pipeline with GitHub Actions
    AWS-ready deployment steps (Lambda & ECS)

Setup & Run Locally

    # Clone repo
    git clone https://github.com/<your-username>/mlops-pipeline.git
    cd mlops-pipeline

    # Create virtual env
    python3 -m venv venv
    source venv/bin/activate

    # Install dependencies
    pip install -r requirements.txt

    # Train model
    python src/train.py

    # Run API
    uvicorn src.app:app --reload

    Open http://127.0.0.1:8000/docs for Swagger UI.
    Docker Build & Run

    docker build -t mlops-fastapi .
    docker run -p 8000:8000 mlops-fastapi

CI/CD Pipeline

    Runs on push to main:

        Install dependencies

        Run tests (pytest)

        Build Docker image

        Push to AWS ECR

    Pipeline file: .github/workflows/ci-cd.yml

AWS Deployment:

Lambda Deployment

    Push image to ECR (handled by CI/CD)

    Create Lambda function from container image

    Attach API Gateway for HTTP access

    Test: POST /predict

ECS Deployment

    Create ECS Cluster (Fargate)

    Create Task Definition using ECR image

    Create Service & attach Load Balancer

    Access via ALB public URL

Future Enhancements

    Add Terraform for Infrastructure as Code

    Add Prometheus/Grafana for monitoring

    Add MLflow for model tracking