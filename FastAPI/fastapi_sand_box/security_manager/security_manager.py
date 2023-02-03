"""
Manejador de elementos de seguridad.
"""

# Fastapi
from fastapi.security import HTTPBearer
from fastapi import status, HTTPException, Request

# token
from jwt_manager import token_manager


class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = token_manager.validate_token(auth.credentials)
        if data["email"] != "admin@email.com":
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Credenciales invalidas.")

