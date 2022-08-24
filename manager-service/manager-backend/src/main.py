from fastapi import FastAPI

app = FastAPI()


@app.get("/manager/api")
def read_root():
    return {"Hello": "World"}