from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/teste1")
async def teste1():
    return {"message": "Hello World from teste1"}

@app.get("/teste2")
async def teste1():
    return {"message": "Segundo teste deu certo!"}