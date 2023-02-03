"""User Model Class User Login"""

# python

# Pydantic
from pydantic import BaseModel, Field


class LoginOut(BaseModel):
    username: str = Field(
        title="User name",
        description="User name",
        min_length=8,
        max_length=20,
        example="John-Doe",
    )
    # mensaje de éxito sign in
    message: str = Field(
        default="Login successful (͠≖ ͜ʖ͠≖)👌", description="Description message"
    )
