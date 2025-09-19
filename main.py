from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return 'heyy'


@app.get("/blog/unpublished")
def unpublished():
    return 'unpublished'


@app.get("/blog/{id}")
def blog(id: int):
    return {'data': id}
