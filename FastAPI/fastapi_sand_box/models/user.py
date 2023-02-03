# User Model

# python
from enum import Enum

# Pydantic
from pydantic import BaseModel, Field, SecretStr, EmailStr


class HairColor(Enum):
    white = "white"
    brown = "brown"
    blonde = "blonde"


class Location(BaseModel):
    city: str = Field(
        title="The City",
        description="The City",
        min_length=3,
        max_length=20,
        example="Queretaro",
    )
    state: str = Field(
        title="The State",
        description="The State",
        min_length=3,
        max_length=20,
        example="Queretaro",
    )
    country: str = Field(
        title="The Country",
        description="The Country",
        min_length=3,
        max_length=20,
        example="Queretaro",
    )


class Person(BaseModel):
    first_name: str = Field(
        title="First name",
        description="First name",
        min_length=8,
        max_length=20,
        example="John Doe",
    )
    last_name: str = Field(
        title="Last name",
        description="Last name",
        min_length=8,
        max_length=20,
        example="Smith",
    )
    age: int = Field(
        default=0, title="The age", description="The age", gt=0, le=100, example="18"
    )
    hair_color: HairColor | None = Field(
        default=None, title="Hair color", description="Hair color", example="white"
    )  # OPTIONAL PARAMETER Y HACE REFERENCIA A LA CLASE HairColor PARA SOLO TOMAR LAS OPCIONES
    is_married: bool | None = Field(
        default=None, title="Is Married", description="Is Married", example="true"
    )  # OPTIONAL PARAMETER
    email: EmailStr = Field(
        title="Email",
        description="Email user",
        example="johndoe@mail.com",
    )
    # password: SecretStr = Field(
    #     title="Password",
    #     description="Password user, minimo 8 caracteres, máximo 20 caracteres",
    #     min_length=8,
    #     max_length=20,
    #     example="DkjS/WhH1pVhZ9oLSluR",
    # )
    password: str = Field(
        title="Password",
        description="Password user, minimo 8 caracteres, máximo 20 caracteres",
        min_length=8,
        max_length=20,
        example="DkjS/WhH1pVhZ9oLSluR",
    )


    # TODO: SE TIENE QUE APLICAR PROCESO DE HASH
