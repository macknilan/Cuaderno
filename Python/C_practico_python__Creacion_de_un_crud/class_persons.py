class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hellow(self):
        print("Hellow, my name is {} and I am {} years old".format(self.name, self.age))


if __name__ == "__main__":
    person = Person("Rodolfo", 39)

    print("Age: {}".format(person.age))
    person.say_hellow()
