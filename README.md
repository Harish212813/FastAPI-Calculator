## Running the Integration Tests

Activate your virtual environment:

```bash
source venv/bin/activate
```

Run all tests:

```bash
pytest
```

This project includes integration tests for:

- User registration
- User login
- Calculation CRUD operations
- Existing calculator endpoints
- Security and validation

## Manual API Testing

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

Open Swagger UI:

```
http://127.0.0.1:8000/docs
```

Use the Swagger interface to test:

- POST /users/register
- POST /users/login
- POST /calculations
- GET /calculations
- GET /calculations/{id}
- PUT /calculations/{id}
- DELETE /calculations/{id}

## Docker Hub

Docker image:

https://hub.docker.com/r/akhil212813/fastapi-calculator