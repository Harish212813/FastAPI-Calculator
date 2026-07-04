# FastAPI Calculator

## Description

This project is a simple calculator web application built using FastAPI. It performs basic arithmetic operations through API endpoints. The project also includes unit tests, integration tests, end-to-end tests using Playwright, logging, and GitHub Actions for continuous integration.

## Features

* Add two numbers
* Subtract two numbers
* Multiply two numbers
* Divide two numbers
* Unit tests with pytest
* Integration tests for API endpoints
* End-to-end tests with Playwright
* Logging
* GitHub Actions workflow

## How to Run the Application

1. Create and activate a virtual environment.

```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install the required packages.

```bash
pip install -r requirements.txt
playwright install
```

3. Start the FastAPI application.

```bash
uvicorn app.main:app --reload
```

4. Open your browser and go to:

```text
http://127.0.0.1:8000/docs
```

## Running the Tests

To run all the tests, use:

```bash
pytest
```

## Technologies Used

* Python
* FastAPI
* Pytest
* Playwright
* Uvicorn
* GitHub Actions
