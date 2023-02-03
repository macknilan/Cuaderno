"""
Router for Authorization
"""

# Python

# Pydantic
from pydantic import SecretStr, Field

# fastpi
from fastapi import APIRouter, status, Form, HTTPException, Body, Path, Request
from fastapi.responses import HTMLResponse, JSONResponse

# Model
from models.user import Person

# token
from jwt_manager import token_manager

router = APIRouter(prefix="/authorization", tags=["Authorization"])


@router.post(
    "/sing-in",
    response_model=Person,
    response_model_exclude={"password"},
    status_code=status.HTTP_200_OK,
    summary="Sing In",
)
async def sing_in(
    email: str = Body(
        embed=True,
        title="Email",
        description="Email user",
        example="admin@email.com",
        min_length=10,
        max_length=100,
    ),
    password: str = Body(
        embed=True,
        title="Password",
        description="Password user",
        example="admin",
        min_length=5,
        max_length=100,
    ),
):
    """
    Servicio que simula el SignIn de usuario y que cumpla el email y password
    en el if
    :param email:
    :param password:
    :return: token
    """
    if email == "admin@email.com" and password == "admin":
        token = token_manager.create_token(
            {"email": "admin@email.com", "password": "admin"}
        )
        return JSONResponse(status_code=status.HTTP_200_OK, content=token)
    else:
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={"message": "Credenciales no validas t(-_-t)"},
        )
