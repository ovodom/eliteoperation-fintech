:::writing{variant="document" id="63821"}
# EliteOperation Fintech API – CI/CD Automation with GitHub Actions and Terraform

## Project Overview

This project demonstrates the development and automation of a containerized Flask API using DevOps practices.

It implements a Continuous Integration (CI) pipeline with GitHub Actions to automatically test the application, validate Terraform infrastructure configuration, and build and test a Docker image.

The Terraform configuration defines AWS infrastructure for a planned deployment. AWS resources have not been provisioned as part of this project.

## Technologies Used

- Python 3.12
- Flask
- Pytest
- Docker
- Terraform
- AWS (infrastructure configuration)
- Git and GitHub
- GitHub Actions

## Project Structure

```text
eliteoperation-fintech/
├── .github/
│   └── workflows/
│       └── ci-cd.yml
├── app/
│   ├── __init__.py
│   ├── main.py
│   └── requirements.txt
├── tests/
│   └── test_app.py
├── terraform/
│   ├── main.tf
│   ├── variables.tf
│   └── outputs.tf
├── Dockerfile
├── .dockerignore
├── .gitignore
├── pytest.ini
└── README.md
```

## Application Endpoints

| Endpoint | Description |
|---|---|
| `/` | Returns the API welcome message |
| `/health` | Checks application health |

## Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/ovodom/eliteoperation-fintech.git
cd eliteoperation-fintech
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r app/requirements.txt
```

### 4. Run the application

```bash
python app/main.py
```

The API will be available at:

- http://localhost:5000/
- http://localhost:5000/health

## Run Tests

```bash
python -m pytest -v
```

## Run with Docker

### Build the Docker image

```bash
docker build -t eliteoperation-fintech:latest .
```

### Start the container

```bash
docker run -d --name eliteoperation-fintech-api -p 5000:5000 eliteoperation-fintech:latest
```

### Test the API

```bash
curl http://localhost:5000/
curl http://localhost:5000/health
```

### Stop and remove the container

```bash
docker stop eliteoperation-fintech-api
docker rm eliteoperation-fintech-api
```

## CI/CD Pipeline

GitHub Actions automatically runs the following jobs when code is pushed to the `main` branch or a pull request is opened against it:

1. **Flask API Tests:** Installs Python dependencies and runs automated tests with Pytest.
2. **Terraform Validation:** Initializes Terraform without configuring a remote backend, checks formatting, and validates the infrastructure configuration.
3. **Docker Build and Integration Tests:** Builds the Docker image, starts a container, and tests the API endpoints.

All three jobs have been successfully executed in GitHub Actions.

## Terraform Infrastructure

The `terraform/` directory contains configuration for:

- AWS security group
- Ubuntu EC2 instance
- Configurable EC2 instance type
- Terraform outputs for instance ID, public IP, and DNS

The infrastructure configuration has been formatted and validated. No AWS resources have been created.

## Project Status

- [x] Flask API development
- [x] Automated application tests
- [x] GitHub repository setup
- [x] GitHub Actions CI workflow
- [x] Terraform infrastructure configuration and validation
- [x] Docker containerization
- [x] Docker integration tests in GitHub Actions
- [ ] Docker Hub image publishing
- [ ] AWS deployment automation

## Author

GitHub: [ovodom](https://github.com/ovodom)
:::
