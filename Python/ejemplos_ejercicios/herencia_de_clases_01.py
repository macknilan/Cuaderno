"""
Programa de ejemplo de herencia de clases.
"""


class Espada:
    def __init__(self, nombre, rareza, dano, durabilidad):
        self.nombre = nombre
        self.rareza = rareza
        self.dano = dano
        self.durabilidad = durabilidad

    def atacar(self, objetivo):
        if self.durabilidad > 0 and objetivo["vida"] > 0:
            objetivo["vida"] -= self.dano + objetivo["resistencia"]
            self.durabilidad -= 0.7
            print(f"self.durabilidad -- > {self.durabilidad}")
        elif objetivo["vida"] <= 0:
            print("El objetivo ha muerto")
        else:
            print("La espada se ha roto")  # durabilidad <= 0


class SuperEspada(Espada):
    def __init__(self, nombre, rareza, dano, durabilidad, atributo, dano_elemental):
        super().__init__(nombre, rareza, dano, durabilidad)
        self.atributo = atributo
        self.dano_elemental = dano_elemental

    def ataqueElemental(self, objetivo):
        if objetivo["Tipo"] == self.atributo:
            objetivo["Vida"] -= self.dano + 35 * self.dano_elemental / 100
            self.durabilidad -= 1
        elif objetivo["Tipo"] != self.atributo:
            objetivo["Vida"] -= self.dano + self.dano_elemental
            self.durabilidad -= 1


if __name__ == "__main__":
    espada_basica = Espada("Espada de Principiante", "Normal", 15, 100)
    print(f"Nombre: {espada_basica.nombre} \nRareza: {espada_basica.rareza}\n")
    espada_basica.atacar({"vida": 1, "resistencia": 1})

    espada_elemental = SuperEspada("Espada Rayo", "Rara", 30, 150, "Rayo", 15)
    print(
        f"Nombre: {espada_elemental.nombre} \nRareza: {espada_elemental.rareza} \nAtributo: {espada_elemental.atributo}\n"
    )
