from fastapi import FastAPI
from utils.calculator import Calculator
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    """
    Simple root endpoint that just returns a message to let the user know
    the server is running.
    """
    return {"message": "Server is running"}

@app.get("/operations/{operation}/{a}/{b}")
async def operations(operation: str, a: float, b: float):
    """
    Perform a mathematical operation between two numbers.

    Args:
    - operation (str): The mathematical operation to perform. One of
      "add", "subtract", "multiply", "divide".
    - a (float): The first number.
    - b (float): The second number.

    Returns:
    - result (float): The result of the operation.
    - error (str): An error message if the operation is invalid.
    """
    calculator = Calculator()
    if operation == "add":
        return {"result": calculator.add(a, b)}
    elif operation == "subtract":
        return {"result": calculator.subtract(a, b)}
    elif operation == "multiply":
        return {"result": calculator.multiply(a, b)}
    elif operation == "divide":
        return {"result": calculator.divide(a, b)}
    else:
        return {"error": "Invalid operation"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
