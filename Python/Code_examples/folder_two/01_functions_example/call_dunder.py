class MyClass:
    def __init__(self, x: int):
        self.x = x

    def __call__(self):
        return self.x


def main():
    obj = MyClass(12)
    print(obj.x)
    print(obj())
    print((2).__class__)
    print(main.__class__)


if __name__ == "__main__":
    main()
