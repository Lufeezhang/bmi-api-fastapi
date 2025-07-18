from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class NumberInput(BaseModel):
    a: float
    b: float

@app.post("/compare")
def compare_numbers(data: NumberInput):
    if data.a > data.b:
        result = f"{data.a} is greater than {data.b}"
    elif data.a < data.b:
        result = f"{data.b} is greater than {data.a}"
    else:
        result = "Both numbers are equal"
    return {"result": result}
