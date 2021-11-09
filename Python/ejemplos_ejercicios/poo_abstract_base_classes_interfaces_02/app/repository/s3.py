from app.repository.user_repository import UserRepository
from app.models.user import User


class S3(UserRepository):
    __clientId: str
    __secretKey: str
    __bucket: str

    def __init__(self, clientId: str, secretKey: str, bucket: str):
        self.__clientId = clientId
        self.__secretKey = secretKey
        self.__bucket = bucket

    def open(self) -> None:
        print(f"Opening connection to AWS S3 {self.__clientId}:{self.__secretKey}")

    def store(self, user: User) -> None:
        user = {"name": user.getName(), "lastName": user.getLastName(), "age": user.getAge()}
        print(f"Storing user from bucket:{self.__bucket}: {user}")

    def close(self) -> None:
        print("Closing connection from AWS S3")
