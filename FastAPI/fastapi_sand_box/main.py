"""
Script de FastAPI de hello word
In Python 3.10.6
Run:
    uvicorn main:app --reload
"""

# fastpi
from fastapi import FastAPI

from routers import sign_in, users, movies, authorization

app = FastAPI(
    # root_path="/api/v1",
    openapi_url="/api/v1/openapi.json",
    title="My App",
    version="0.0.1",
    description="My description",
    contact={"name": "mack", "url": "http://mack.host"},
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)

app.include_router(users.router)
app.include_router(sign_in.router)
app.include_router(movies.router)
app.include_router(authorization.router)
