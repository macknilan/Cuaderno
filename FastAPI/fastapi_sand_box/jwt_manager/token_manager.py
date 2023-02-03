"""
Manager for tokens
"""
import os
from jwt import encode, decode
from dotenv import load_dotenv


BASE_DIR = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
ENV_DIR = os.path.join(BASE_DIR, ".envs")

load_dotenv(os.path.join(ENV_DIR, ".env"))


def create_token(data: dict) -> str:
    # print("DEBUGGER")
    token: str = encode(payload=data, key=os.getenv("SECRET_KEY"), algorithm="HS256")

    return token


def validate_token(token: str) -> dict:
    # print("DEBUGGER")
    data: dict = decode(token, key=os.getenv("SECRET_KEY"), algorithms=["HS256"])

    return data

