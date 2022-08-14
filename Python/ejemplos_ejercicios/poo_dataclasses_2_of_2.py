"""
https://youtu.be/rdRLfgVp8O0
Ejemplo 01 de Dataclasses
Como se puede hacer una clase y después como se puede hacer por Dataclasses

Particularmente adecuado para modelar clases que representan datos y,
como tales, ofrecen mecanismos fáciles para inicializar,
imprimir, ordenar, ordenar y comparar datos.
"""
import dataclasses
from dataclasses import dataclass


@dataclass
class OtherUser:
    username: str
    email: str = None
    last_login: int = 10


other = OtherUser("mack")
other.username
