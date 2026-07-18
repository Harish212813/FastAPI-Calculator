# FastAPI Calculator

## Overview

This project is a FastAPI calculator application that has been built throughout the course. It includes calculator endpoints, PostgreSQL database integration, user authentication, password hashing, calculation CRUD operations, automated testing, Docker support, and GitHub Actions for CI/CD.

## Features

- Basic calculator operations
  - Add
  - Subtract
  - Multiply
  - Divide
- FastAPI REST API
- User registration
- User login with password verification
- Calculation CRUD operations
  - Create
  - Browse
  - Read
  - Update
  - Delete
- PostgreSQL database
- SQLAlchemy ORM
- Pydantic validation
- Password hashing using bcrypt
- Integration tests with pytest
- Docker support
- GitHub Actions CI/CD
- Docker Hub deployment

## Requirements

- Python 3.11+
- PostgreSQL
- Docker Desktop (optional)
- Git

## Installation

Clone the repository:

```bash
git clone https://github.com/Harish212813/FastAPI-Calculator.git
```

Go into the project folder:

```bash
cd FastAPI-Calculator
```

Create and activate a virtual environment:

### macOS/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## Running the Application

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

Open your browser:

```
http://127.0.0.1:8000/docs
```

Swagger UI can be used to test all API endpoints.

## Running Tests

Run all tests with:

```bash
pytest
```

The project includes unit tests and integration tests for:

- Calculator operations
- User registration
- User login
- Calculation CRUD endpoints
- Security
- Pydantic schemas

## Manual API Testing

After starting the application, open:

```
http://127.0.0.1:8000/docs
```

From Swagger you can test:

- POST /users/register
- POST /users/login
- POST /calculations
- GET /calculations
- GET /calculations/{id}
- PUT /calculations/{id}
- DELETE /calculations/{id}

## Docker

Build the Docker image:

```bash
docker build -t fastapi-calculator .
```

Run the application:

```bash
docker compose up --build
```

## Docker Hub

Docker image:

https://hub.docker.com/r/akhil212813/fastapi-calculator

## GitHub Actions

GitHub Actions automatically:

- Runs all tests
- Starts a PostgreSQL service for testing
- Builds the Docker image
- Pushes the latest image to Docker Hub after successful tests

## Project Structure

```
fastapi-calculator/
│
├── app/
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   ├── operations.py
│   ├── schemas.py
│   ├── security.py
│   └── services/
│       └── calculation_factory.py
│
├── tests/
│   ├── test_user_routes.py
│   ├── test_calculation_routes.py
│   ├── test_operations.py
│   ├── test_security.py
│   ├── test_schemas.py
│   └── ...
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

