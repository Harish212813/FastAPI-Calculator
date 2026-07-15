# FastAPI Calculator

## Overview

This project is a FastAPI calculator application that has been built throughout the course. It includes calculator endpoints, PostgreSQL database integration, a secure user model using SQLAlchemy, a Calculation model, password hashing, Pydantic validation, automated testing, Docker support, and GitHub Actions for CI/CD.

## Features

- Basic calculator operations
  - Add
  - Subtract
  - Multiply
  - Divide
- FastAPI REST API
- SQLAlchemy User model
- SQLAlchemy Calculation model
- PostgreSQL database
- Password hashing using Passlib
- Pydantic input validation
- Calculation validation with Pydantic
- Calculation Factory pattern
- Unit and integration tests with Pytest
- Docker support
- GitHub Actions CI/CD pipeline
- Docker Hub image deployment

## Technologies Used

- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- Pydantic
- Pytest
- Docker
- GitHub Actions

## Running the Application

Clone the repository:

```bash
git clone https://github.com/Harish212813/FastAPI-Calculator.git
cd FastAPI-Calculator
```

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Start the application:

```bash
uvicorn app.main:app --reload
```

Open your browser and go to:

```
http://127.0.0.1:8000/docs
```

to access the Swagger API documentation.

## Running Tests Locally

Run all tests:

```bash
pytest -v
```

Run tests with coverage:

```bash
pytest --cov=app --cov-report=term-missing
```

## Docker

Build the Docker image:

```bash
docker build -t fastapi-calculator .
```

Run the Docker container:

```bash
docker run -p 8000:8000 fastapi-calculator
```

## Docker Hub

Docker image:

https://hub.docker.com/r/akhil212813/fastapi-calculator

## GitHub Repository

https://github.com/Harish212813/FastAPI-Calculator

## Testing

This project includes:

- Unit tests
- Integration tests
- API endpoint testing
- Password hashing tests
- User validation tests
- Database testing
- Calculation factory tests
- Calculation schema validation tests
- Calculation model integration tests

All tests are automated using GitHub Actions.

## Module 11: Calculation Model

This project now includes a SQLAlchemy Calculation model with the following fields:

- id
- a
- b
- type
- result

Pydantic schemas are used to validate calculation input and output. The supported calculation types are Add, Sub, Multiply, and Divide. Division by zero and unsupported calculation types are rejected.

A calculation factory is also included to perform the correct operation based on the selected calculation type.

## Running the Module 11 Tests

Activate the virtual environment:

```bash
source venv/bin/activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run all tests:

```bash
pytest
```

Run tests with coverage:

```bash
pytest --cov=app --cov-report=term-missing
```