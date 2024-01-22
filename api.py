from fastapi import FastAPI
app = FastAPI()
import datetime
import random

@app.get("/")
async def myfync():
    return datetime.datetime.now()

@app.get("/test1")
async def myfync():
    number = random.randint(0,1000000)
    return str(number)