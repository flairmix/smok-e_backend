from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from . import models
from .database import engine
from .routers import auth, todos, admin, users, smoke, converter
from datetime import datetime

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000", "http://127.0.0.1:8080", 'http://localhost:8080'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
app.include_router(users.router)
app.include_router(smoke.router)
app.include_router(converter.router)


@app.get('/')
async def read_main():
    return {"msg" : "Hello World"}


@app.get("/day", tags=["Dates"])
def get_day_of_week():
    """
    Get the current day of week
    """
    return {
        "day": datetime.now().strftime("%A")
    }


@app.get("/hello/{name}")
async def say_hello():
    return {"name": "hello {name}"}



