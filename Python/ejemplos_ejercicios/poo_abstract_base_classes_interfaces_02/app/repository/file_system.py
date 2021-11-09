from app.repository.user_repository import UserRepository
from app.models.user import User


class FileSystem(UserRepository):
    __directory: str

    def __init__(self, directory: str):
        self.__directory = directory

    def open(self) -> None:
        print(f"Opening directory: {self.__directory}")

    def store(self, user: User) -> None:
        xml = f"<root><name>{user.getName()}</name><lastName>{user.getLastName()}</lastName><age>{user.getAge()}</age></root>"
        print(f"Storing user in file :{self.__directory}/{user.getName()}")
        print(xml)

    def close(self) -> None:
        print("Closing file")
