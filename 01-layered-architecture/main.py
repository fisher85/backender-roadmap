from fastapi import Body, FastAPI
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from math import sqrt
import uvicorn


app = FastAPI()
app.mount("/public", StaticFiles(directory="public"), name="public")


@app.get("/")
async def read_index():
    return RedirectResponse(url="/public/index.html")


@app.get("/square_root/{number}")
async def square_root(number: float):
    return sqrt(number)


@app.post("/square_root")
async def square_root2(number: float = Body(embed=True)):
    return sqrt(number)


@app.post("/secret_func")
async def secret_func(first: int = Body(embed=True), second: int = Body(embed=True)):
    return {'answer': 'Bad input' if second < 0 else first + second}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="debug")
