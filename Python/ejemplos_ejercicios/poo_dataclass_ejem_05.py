# https://www.youtube.com/watch?v=vRVVyl9uaZc
# https://realpython.com/python-data-classes/
# https://github.com/mCodingLLC/VideosSampleCode

import dataclasses
import inspect
from dataclasses import dataclass, field
from pprint import pprint
from typing import List


@dataclass()
class Person:
    """dataclass Person"""

    sort_index: int = field(
        init=False, repr=False
    )  # ORDENAR LA CLASE SE TIENE QUE INICIALISAR EN FALSO USANDO LA FUNCION field, repr=False PARA QUE SE DE LA REPRESENTACION CUANDO SE IMPRIMA Person(name='Geralt', job='Witcher', age=30)
    name: str
    job: str
    age: int
    value_by_default: int = 100

    def __post_init__(self):
        """ORDENAR POR LA EDAD.
        sort_index ESTA SIDNO USADO POR DATACLASS COMO MIEMBRE DE LA CLASE
        """
        self.sort_index = self.age

    # def __str__(self):
    #     return f"{self.name}, {self.job} ({self.age})"


person1 = Person("Geralt", "Witcher", 30)
person2 = Person("Yennefer", "Sorceress", 25)
person3 = Person("Yennefer", "Sorceress", 25)

print(person1)
print(id(person2))
print(id(person3))
print(
    person3 == person2
)  # TRUE person2 = Person("Yennefer", "Sorceress", 25) == person3 = Person("Yennefer", "Sorceress", 25)
