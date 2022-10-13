from fastapi import FastAPI

app = FastAPI()

@app.get("/suma")
async def sum(a: int, b: int):
    return a+b

