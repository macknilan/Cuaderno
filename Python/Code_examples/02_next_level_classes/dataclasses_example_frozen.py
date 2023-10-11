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

# -frozen=True- LO QUE HACE ES "CONGELAR QUE NO SE MODIFIQUE LOS DATOS QUE SE CREAN DE LA CLASE"
@dataclass(frozen=True)
class Person:
    name: str
    address: str
    active: bool = True
    email_addresses: list[str] = field(default_factory=list)  # SE DEFINE UNA LISTA VACÍA CON -field-
    id: str = field(init=False, default_factory=generate_id)  # -init=False- ES PARA NO INICIALIZAR -id- AL MOMENTO DE
    # CREAR -Person-
    _search_string: str = field(init=False, repr=False)  # -repr=False- ES PARA QUE NO SE IMPRIMA AL MOMENTO DE LLAMAR
    # LA CLASE -Person-


def main() -> None:
    person = Person(name="John", address="123 Main St")
    person.name = "Mack"  # NO ES POSIBLE CON -frozen=True-
    print(person)


if __name__ == "__main__":
    main()
