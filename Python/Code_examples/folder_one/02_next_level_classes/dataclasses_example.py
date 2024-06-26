import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    return "".join(random.choices(string.ascii_uppercase, k=12))


class PersonNoDataClass:
    def __init__(self, name: str, address: str):
        self.id = generate_id()
        self.name = name
        self.address = address
        self.email_addresses = []


@dataclass
# @dataclass(kw_only=True)  # -kw_only=True- ES PARA QUE LOS ARGUMENTOS SEAN SOLO POR NOMBRE
class Person:
    name: str
    address: str
    active: bool = True
    email_addresses: list[str] = field(default_factory=list)  # SE DEFINE UNA LISTA VACÍA CON -field-
    id: str = field(init=False, default_factory=generate_id)  # -init=False- ES PARA NO INICIALIZAR -id- AL MOMENTO DE
    # CREAR -Person-
    _search_string: str = field(init=False, repr=False)  # -repr=False- ES PARA QUE NO SE IMPRIMA AL MOMENTO DE LLAMAR
    # LA CLASE -Person-

    def __post_init__(self):
        """
        FUNCIÓN QUE SE EJECUTA DESPUÉS DE EJECUTAR LA CLASE -Person-
        Y ASIGNAR A -_search_string- EL VALOR COMBINADO DE -name- -address-
        :return:
        """
        self._search_string = f"{self.name} {self.address}"

    def __str__(self) -> str:
        """
        FUNCIÓN QUE SE EJECUTA AL LLAMAR LA CLASE -Person- CON -print-
        :return:
        """
        return f"{self.name} ({self.id})"


def main() -> None:
    person = Person(name="John", address="123 Main St")
    print(person)
    print(repr(person))
    print(f"{person}")
    print(f"{person!r}")


if __name__ == "__main__":
    main()
