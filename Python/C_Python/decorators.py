PASSWORD = "12345"


def password_required(func):
    def wrapper():
        password = input("¿Cual es la contrasena?: ")

        if password == PASSWORD:
            return func()  # SE REGRESA LA SEÑAL
        else:
            print("La contrasena no es correcta.")

    return wrapper


@password_required
def needs_password():
    print("La contrasena es correcta.")


def upper(func):
    def wrapper(*args, **kwargs):
        # import pdb; pdb.set_trace()
        result = func(*args, **kwargs)

        return result.upper()

    return wrapper


@upper
def say_my_name(name):
    return "Hola {}".format(name)


if __name__ == "__main__":
    print(say_my_name("mack"))
# if __name__ == '__main__':
#     needs_password()
