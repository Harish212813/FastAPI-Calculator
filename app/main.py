# app/main.py

import logging
from fastapi import FastAPI, HTTPException
from app.operations import add, subtract, multiply, divide

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
        raise HTTPException(status_code=400, detail="Cannot divide by zero.")