# polimorfirmo


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Meow")


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Bark")


if __name__ == "__main__":

    cat1 = Cat("Kitty", 2.5)
    dog1 = Dog("Fluffy", 4)

    for animal in (cat1, dog1):
        animal.make_sound()
        animal.info()
        animal.make_sound()

# out
# Meow
# I am a cat. My name is Kitty. I am 2.5 years old.
# Meow
# Bark
# I am a dog. My name is Fluffy. I am 4 years old.
# Bark
