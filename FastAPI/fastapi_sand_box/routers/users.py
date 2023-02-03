"""Router Users"""

# Pydantic
from pydantic import EmailStr

# fastpi
from fastapi import (
    APIRouter,
    status,
    Path,
    Query,
    Form,
    Header,
    Cookie,
    UploadFile,
    HTTPException,
)

# Models
from models.user import Location, Person

router = APIRouter(prefix="/users", tags=["Users"])

# ROUTES


@router.get("/", summary="First service for testing", status_code=status.HTTP_200_OK)
async def home():
    """
    Endpoint for test Hellow Word

    :return: {"Hello": "World"}
    """
    return {"Hello": "World"}


@router.post(
    "/add",
    response_model=Person,
    response_model_exclude={"password"},
    status_code=status.HTTP_201_CREATED,
    summary="Add new user/person",
)
async def add_person(person: Person):
    """
    Endpoint for add person

    :param person:

    :return: person, exclude password
    """
    return person


# Validaciones Query Parameters
@router.get(
    "/detail", status_code=status.HTTP_200_OK, summary="Get detail user/person by ID"
)
async def detail_person(
    name: str
    | None = Query(
        default=None,
        min_length=8,
        max_length=50,
        title="Person name title",
        description="It's between 1 and 50 characters.",
    ),  # QUERY PARAMETERS OPCIONAL
    age: int = Query(
        gt=0,
        le=100,
        title="Person age title",
        description="This is the person age. It's required.",
    ),  # QUERY PARAMETERS OBLIGATORIO
):
    """
    Endpoint for test Query parameters

    :param name:

    :param age:

    :return: {name: age}

    """
    return {name: age}


# Validación Path Parameters
persons = [1, 2, 3, 4, 5]


@router.get(
    "/detail/{person_id}",
    status_code=status.HTTP_200_OK,
    summary="Get detail user/person by ID",
)
async def detail_person(
    person_id: int = Path(
        gt=0,
        title="Title the ID of the item(person) to get title",
        description="This is the ID person. It's required",
    )
):
    """
    Endpoint for get user with ID
    Validación Path Parameters con HTTPException
    :param person_id:
    :return: {person_id: "It exist"}
    """
    if person_id not in persons:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Person not found t(-_-t)."
        )
    return {person_id: "It exist"}


# PRIMERA OPCIÓN
@router.put("/detail-one/{person_id}", deprecated=True)
async def update_person(
    person: Person,
    location: Location,
    person_id: int = Path(
        gt=0,
        title="The ID of the item(person) to get title",
        description="This is the ID person. It's required.",
    ),
):
    results = person.dict()
    results.update(location.dict())
    return results


# SEGUNDA OPCIÓN
@router.put("/detail-two/{person_id}", deprecated=True)
async def update_person(
    person_id: int,
    person: Person,
    location: Location,
):
    results = {"person_id": person_id, "person": person, "location": location}
    return results


# TERCERA OPCIÓN
@router.put(
    "/detail/{person_id}", status_code=status.HTTP_200_OK, summary="Update user/person"
)
async def update_person(
    person: Person,
    location: Location,
    person_id: int = Path(
        gt=0,
        title="The ID of the item(person) to get title",
        description="This is the ID person. It's required.",
        example=1,
    ),
):
    """
    Service for update user

    :param person:

    :param location:

    :param person_id:

    :return: {"person_id": person_id, "person": person, "location": location}

    """
    results = {"person_id": person_id, "person": person, "location": location}
    return results


# Cookies and Headers Parameters
@router.post("/contact", status_code=status.HTTP_200_OK, summary="Send contact form.")
async def contact(
    first_name: str = Form(max_length=20, min_length=8),
    email: EmailStr = Form(),
    message: str = Form(min_length=20),
    # No obligatorio y de tipo header
    user_agent: str | None = Header(default=None),
    ads: str | None = Cookie(default=None),
):
    """
    Servicio como ejemplo de headers y cookies que regresa el mensaje de quien lo envío.

    :param first_name:

    :param email:

    :param message:

    :param user_agent:

    :param ads:

    :return: # "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
    """
    return user_agent


# Upload files
@router.post("/post-image", status_code=status.HTTP_200_OK, summary="Upload a image")
async def post_image(image: UploadFile):
    """
    Ejemplo de subir imágenes

    :param image:

    :return: filename, format, Size(kb)
    """
    return {
        "filename": image.filename,
        "format": image.content_type,
        "Size(kb)": str(round(len(image.file.read()) / 1024, ndigits=2)) + " kb",
    }
