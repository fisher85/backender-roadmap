from fastapi import Body, FastAPI
from fastapi.responses import HTMLResponse
from math import sqrt
import uvicorn


app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def read_root():
    return """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Hello, world!</h1>
        </body>
        <script type="text/javascript">
            function changeHeader() {
                let h1 = document.querySelector('h1');
                h1.innerHTML = '3 seconds have passed!';
            }
            setTimeout(changeHeader, 3000);
        </script>
    </html>
    """


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: int):
    return {"item_id": item_id, "q": q}


@app.post("/square_root")
async def square_root(number: int = Body(embed=True)):
    return sqrt(number)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="debug")
