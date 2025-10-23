from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <head>
            <title>Shirt Designer</title>
        </head>
        <body style="text-align: center; font-family: sans-serif;">
            <h1>Welcome to the Shirt Designer!</h1>
            <p>This site is powered by <b>FastAPI</b> and hosted on <b>Wasmer</b>.</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
