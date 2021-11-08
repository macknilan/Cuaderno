
class User:
    __name: str
    __lastName: str
    __age: int

    def __init__(self, name: str, lastName: str, age: int):
        self.__name = name
        self.__lastName = lastName
        self.__age = age

    def getName(self) -> str:
        return self.__name

    def getLastName(self) -> str:
        return self.__lastName

    def getAge(self) -> int:
        return self.__age
