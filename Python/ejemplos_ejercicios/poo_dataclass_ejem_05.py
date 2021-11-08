
# https://www.youtube.com/watch?v=vRVVyl9uaZc
# https://realpython.com/python-data-classes/
# https://github.com/mCodingLLC/VideosSampleCode

import dataclasses
import inspect
from dataclasses import dataclass, field
from typing import List
from pprint import pprint

from dataclasses import dataclass, field

@dataclass()
class Person:
    name: str
    job: str
    age: int

    def __str__(self):
        return f'{self.name}, {self.job} ({self.age})'


person1 = Person("Geralt", "Witcher", 30)
person2 = Person("Yennefer", "Sorceress", 25)
person3 = Person("Yennefer", "Sorceress", 25)

print(person1)
print(id(person2))
print(id(person3))
print(person3 == person2)

