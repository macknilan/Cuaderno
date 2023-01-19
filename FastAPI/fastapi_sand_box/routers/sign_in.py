"""
Router for Sign In
"""

# Pydantic
from pydantic import SecretStr

# fastpi
from fastapi import APIRouter, status, Form

# Models
from models.user_login import LoginOut

router_sing_in = APIRouter(prefix="/sign-in", tags=["Sign In"])


# Data Forms
@router_sing_in.post(
    "/",
    response_model=LoginOut,
    response_model_exclude={"password"},
    status_code=status.HTTP_200_OK,
    summary="Sing In"
)
async def login(username: str = Form(), password: SecretStr = Form()):
    """
    Servicio para login por medio de data form

    :param username:
    :param password:
    :return: { "username": "werouwoeriu",  "message": "Login successful (͠≖ ͜ʖ͠≖)👌"}
    """
    # return {"username": username}
    return LoginOut(username=username)
