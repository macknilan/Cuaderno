"""
Programa de ejemplo de herencia de clases.
"""


# Creamos una clase padre llamada "Animal"
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("{} makes a noise.".format(self.name))


# Creamos una clase hija llamada "Dog" que hereda de la clase "Animal"
class Dog(Animal):
    def __init__(self, name, breed):
        # Llamamos al método __init__ de la clase padre
        super().__init__(name)
        self.breed = breed

    # Sobrescribimos el método "speak" de la clase padre
    def speak(self):
        print("{} barks.".format(self.name))


# Creamos una instancia de la clase "Dog"
dog = Dog("Max", "Golden Retriever")

# Llamamos al método "speak" de la clase "Dog"
dog.speak()
