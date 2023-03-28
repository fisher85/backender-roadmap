from fastapi import Body, FastAPI
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from math import sqrt
import hypercorn
import uvicorn
import asyncio
from hypercorn.config import Config
from hypercorn.asyncio import serve


app = FastAPI()
app.mount("/public", StaticFiles(directory="public"), name="public")


@app.get("/")
async def read_index():
    return RedirectResponse(url="/public/index.html")


@app.get("/square_root/{number}")
async def square_root(number: float):
    return sqrt(number)


@app.post("/square_root")
async def square_root(number: float = Body(embed=True)):
    return sqrt(number)


if __name__ == "__main__":
    config = Config()
    config.host = ["127.0.0.1:8000"]
    config.loglevel = 'debug'
    config.keyfile = 'key.pem'
    config.certfile = 'cert.pem'
    asyncio.run(serve(app, config))
