class MyClass:
    def __init__(self, x: int):
        self.x = x

    def __call__(self):
        return self.x


def main():
    obj = MyClass(12)
    print(f"obj.x -> {obj.x}")
    print(f"El método __call__ llama al objeto obj() -> {obj()}")
    print(f"El método __call__ llama al objeto obj.__call__() 2 -> {obj.__call__()}")

    # IMPRIME EL TIPO DE DATO DE LOS OBJETOS, DOS ES UN ENTERO Y ES UN OBJETO
    print((2).__class__)

    # IMPRIME LA CLASE DE MAIN QUE ES UNA FUNCIÓN
    print(main.__class__)


if __name__ == "__main__":
    main()
