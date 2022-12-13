"""
EJEMPLO DE @dataclasses
"""

import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    return "".join(random.choices(string.ascii_uppercase, k=12))


# @dataclass(frozen=True)
# -frozen=True- hace que los atributos de la clase no sean mutables, los valores con los que sé
# iniciaron al momento de crear la clase -Person-
# -@dataclass(kw_only=True)- 3.10 FUERZA a que al momento de inicializar el objeto -Person- sea con llave valor
# -Person(name="Rodolfo", address="123 calle siempre viva")-
@dataclass(kw_only=True, slots=True)
class Person:
    """
    De forma implicita se genera __repr__

    """

    name: str
    address: str
    active: bool = True  # valor por defecto(True) y no se tienen que declarar cuando se crea el objeto Person
    email_addressess: list[str] = field(default_factory=list)
    # 👆 El parámetro es una lista de strings, que es diferente para cada objeto que se cree.
    id: str = field(init=False, default_factory=generate_id)
    # 👆 El parámetro de tipo string es diferente para cada objeto que se cree y por default
    # se crea un valor random por medio de la función
    # -init=False- ocasiona que no se inicialice al momento de crear el objeto -Person- ❌ id="CHKWKFCGSNPY"
    # y que se cree por default por medio de la función.
    _search_string: str = field(init=False, repr=False)

    def __post_init__(self) -> None:
        self._search_string = f"{self.name} {self.address}"
        # 👆 El atributo de la clase -search_string- con el método predefinido -__post_init__- se le asigna un
        # valor después de crear el objeto con los atributos -name- y -address-
        # -repr=False- indica que oculta el atributo al momento de imprimir la instancia del objeto -Person-
        # pero sigue siendo parte de la clase.


def main() -> None:
    person = Person(name="Rodolfo", address="123 calle siempre viva")
    # print(person.__dict__["name"])
    # 👆 -slots=False- permite imprimir de esta forma
    print(person.__dir__())
    # 👆 -slots- en dataclass hacen posible -> @dataclass(slots=True) LAS CLASES SON MUCHO MÁS RÁPIDAS 👀
    # ❌ No utilizar con herencia multiple -slots-.
    print(person.name)
    print(person)


if __name__ == "__main__":
    main()
