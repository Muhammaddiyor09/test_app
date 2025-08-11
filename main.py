from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from db import engine, Base
from routers.users import users_router
from routers.login import login_router
from routers.science import router as science
from routers.lesson import router as lesson
from routers.information import router as information
from routers.test import router as test


description = """
------------------------------
**Username and password for Admin**
* Login: **md**
* Parol: **mmd**
------------------------------
"""

app = FastAPI(
    description=description,
    docs_url='/',
    redoc_url='/redoc',
)

Base.metadata.create_all(bind=engine)


app.include_router(users_router)
app.include_router(login_router)
app.include_router(science)
app.include_router(lesson)
app.include_router(information)
app.include_router(test)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)