"""
Model for movies
"""

# Pydantic
from pydantic import BaseModel, Field, validator


class Movies(BaseModel):
    id: int = Field(
        title="Id Movie",
        description="ID of the movie",
        gt=0,
        le=100,
    )
    title: str = Field(
        title="Title movie",
        description="Title of the movie",
        min_length=3,
        max_length=100,
    )
    overview: str = Field(
        title="Overview",
        description="Description of the movie",
        min_length=6,
        max_length=100,
    )
    year: int = Field(
        title="Year",
        description="Year of release",
    )
    rating: float = Field(
        title="Rating",
        description="Rating of the movie",
        gt=0,
        le=10,
    )
    category: str = Field(
        title="Category",
        description="Category of the movie",
        min_length=3,
        max_length=100,
    )

    @validator("year")
    def year_is_valid(cls, value):
        if not (1800 <= value <= 2023):
            raise ValueError("Year must be a 4 digit number between 1800 and 2023.")
        return value

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "title": "Jumanji",
                "overview": "Description of the movie",
                "year": 2022,
                "rating": 7.8,
                "category": "Sci-fi/Adventure"
            }
        }
