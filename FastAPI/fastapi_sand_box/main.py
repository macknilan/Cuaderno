"""
Script de FastAPI de hello word

Run:
    uvicorn main:app --reload
"""
# python


# Pydantic
from pydantic import BaseModel, Field

# fastpi
from fastapi import FastAPI, Path, Query

app = FastAPI()

# models
class Location(BaseModel):
    city: str = Field(
        title="The City", description="The City", min_length=8, max_length=20
    )
    state: str = Field(
        title="The State", description="The State", min_length=8, max_length=20
    )
    country: str = Field(
        title="The Country", description="The Country", min_length=8, max_length=20
    )


class Person(BaseModel):
    first_name: str = Field(
        title="First name", description="First name", min_length=8, max_length=20
    )
    last_name: str = Field(
        title="Last name", description="Last name", min_length=8, max_length=20
    )
    age: int = Field(default=0, title="The age", description="The age", gt=0, le=100)
    hair_color: str | None = Field(
        default=None, title="Hair color", description="Hair color", max_length=20
    )  # optional parameter
    is_married: bool | None = Field(
        default=None, title="Is Married", description="Is Married"
    )  # optional parameter


@app.get("/")
async def home():
    return {"Hello": "World"}


@app.post("/person/add")
async def add_person(person: Person):
    return person


@app.get("/person/detail")
async def detail_person(
    name: str
    | None = Query(
        default=None,
        min_length=8,
        max_length=50,
        title="Person name title",
        description="It's between 1 and 50 characters.",
    ),  # Query Parameters opcional
    age: int = Query(
        gt=0,
        le=100,
        title="Person age title",
        description="This is the person age. It's required.",
    ),  # Query Parameters obligatorio
):
    return {name: age}


@app.get("/person/detail/{person_id}")
async def detail_person(
    person_id: int = Path(
        gt=0,
        title="The ID of the item(person) to get title",
        description="This is the ID person. It's required.",
    )
):
    return {person_id: "It exist"}


# PRIMERA OPCIÓN
# @app.put("/person/detail/{person_id}")
# async def update_person(
#     person: Person,
#     location: Location,
#     person_id: int = Path(
#         gt=0,
#         title="The ID of the item(person) to get title",
#         description="This is the ID person. It's required.",
#     ),
# ):
#     results = person.dict()
#     results.update(location.dict())
#     return results


# SEGUNDA OPCIÓN
# @app.put("/person/detail/{person_id}")
# def update_person(
#     person_id: int,
#     person: Person,
#     location: Location,
# ):
#     results = {"person_id": person_id, "person": person, "location": location}
#     return results


# TERCERA OPCIÓN
@app.put("/person/detail/{person_id}")
def update_person(
    person: Person,
    location: Location,
    person_id: int = Path(
        gt=0,
        title="The ID of the item(person) to get title",
        description="This is the ID person. It's required.",
    ),
):
    results = {"person_id": person_id, "person": person, "location": location}
    return results
