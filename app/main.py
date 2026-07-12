import logging

from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import User
from app.operations import add, divide, multiply, subtract
from app.schemas import UserCreate, UserRead
from app.security import hash_password


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()


@app.get("/")
def home():
    logger.info("Home endpoint was called")
    return {"message": "FastAPI Calculator is running"}


@app.get("/add")
def add_numbers(a: float, b: float):
    result = add(a, b)
    logger.info(f"Add operation: {a} + {b} = {result}")
    return {"operation": "add", "result": result}


@app.get("/subtract")
def subtract_numbers(a: float, b: float):
    result = subtract(a, b)
    logger.info(f"Subtract operation: {a} - {b} = {result}")
    return {"operation": "subtract", "result": result}


@app.get("/multiply")
def multiply_numbers(a: float, b: float):
    result = multiply(a, b)
    logger.info(f"Multiply operation: {a} * {b} = {result}")
    return {"operation": "multiply", "result": result}


@app.get("/divide")
def divide_numbers(a: float, b: float):
    try:
        result = divide(a, b)
        logger.info(f"Divide operation: {a} / {b} = {result}")
        return {"operation": "divide", "result": result}
    except ValueError:
        logger.error("Division by zero attempted")
        raise HTTPException(
            status_code=400,
            detail="Cannot divide by zero.",
        )


@app.post(
    "/users",
    response_model=UserRead,
    status_code=status.HTTP_201_CREATED,
)
def create_user(user_data: UserCreate, db: Session = Depends(get_db)):
    existing_username = (
        db.query(User)
        .filter(User.username == user_data.username)
        .first()
    )

    if existing_username:
        raise HTTPException(
            status_code=400,
            detail="Username already exists.",
        )

    existing_email = (
        db.query(User)
        .filter(User.email == user_data.email)
        .first()
    )

    if existing_email:
        raise HTTPException(
            status_code=400,
            detail="Email already exists.",
        )

    new_user = User(
        username=user_data.username,
        email=user_data.email,
        password_hash=hash_password(user_data.password),
    )

    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail="Username or email already exists.",
        )

    logger.info(f"New user created: {new_user.username}")
    return new_user