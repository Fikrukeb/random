from fastapi import FastAPI
import random
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/random")
async def say_hello(min: int = 0, max:int=7):
    my_list = list(range(min, max))

    random.shuffle(my_list)
    return {"orders": my_list}
