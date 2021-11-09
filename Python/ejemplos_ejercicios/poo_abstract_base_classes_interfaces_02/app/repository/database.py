from app.repository.user_repository import UserRepository
from app.models.user import User


class Database(UserRepository):
    __host: str
    __user: str
    __password: str

    def __init__(self, host: str, user: str, password: str):
        self.__host = host
        self.__user = user
        self.__password = password

    def open(self) -> None:
        print(f"Opening database connection: {self.__host}:{self.__user}@{self.__password}")

    def store(self, user: User) -> None:
        userElements = {"name": user.getName(), "lastName": user.getLastName(), "age": user.getAge()}
        print(f"Storing user in the database {user.getName()}\n")
        print(f"INSERT INTO USER VALUES('{userElements['name']}','{userElements['lastName']}',{userElements['age']})")

    def close(self) -> None:
        print("Closing connection")
