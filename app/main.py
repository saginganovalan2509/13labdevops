from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Лабораторная работа 13 по DEVOPS!"}

@app.get("/hello/{name}")
def read_item(name: str):
    return {"message": f"Привет, {name}!"}
