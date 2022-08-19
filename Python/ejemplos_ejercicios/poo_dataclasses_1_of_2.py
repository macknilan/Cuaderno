"""
https://youtu.be/rdRLfgVp8O0
Ejemplo 01 de Dataclasses
Como se puede hacer una clase y después como se puede hacer por Dataclasses

Particularmente adecuado para modelar clases que representan datos y,
como tales, ofrecen mecanismos fáciles para inicializar,
imprimir, ordenar, ordenar y comparar datos.
"""


class OtherUser:
    username: str
    email: str = None
    last_login: int = 10

    def __init__(self, username: str, email: str = None, last_login: str = 10):
        self.username = username
        self.email = email
        self.last_login = last_login


other = OtherUser("mack")
other.username
