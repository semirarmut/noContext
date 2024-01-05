import uvicorn
from fastapi import FastAPI

from routers import hello_world

app = FastAPI(title='NO CONTEXT')


@app.get("/")
def root():
    return "NO CONTEXT"


app.include_router(hello_world.router)

host = "127.0.0.1"
port = 8080

if __name__ == "__main__":
    uvicorn.run("main:app", host=host, port=port, reload=True)
