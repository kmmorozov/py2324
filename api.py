from fastapi import FastAPI
app = FastAPI()
import datetime
@app.get("/")
async def myfync():
    return datetime.datetime.now()

@app.get("/test1")
async def myfync():
    return "kirill"