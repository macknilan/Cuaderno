"""
Ejemplo para entender
Getters y Setters en python
Con el decorador @property
"""


class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    # método getter para name
    @property
    def name(self):
        return self._name

    # método setter para el nombre
    @name.setter
    def name(self, name):
        self._name = name

    # método getter para age
    @property
    def age(self):
        return self._age

    # método setter para age
    @age.setter
    def age(self, age):
        self._age = age


def main():
    # se crea una instancia pra la clase Person
    person = Person("John", 30)

    # "Get" name y age para person
    print(person.name)  # Output: "John"
    print(person.age)  # Output: 30

    # "Set" name y age para person
    person.name = "Jane"
    person.age = 25

    # "Get" el nuevo valor de name y age para person
    print(person.name)  # Output:


if __name__ == "__main__":
    main()
