import sys
import csv
import os

CLIENT_TABLE = ".clients.csv"
CLIENT_SCHEMA = ["name", "company", "email", "position"]
clients = []


def _initialize_clients_from_storage():
    with open(CLIENT_TABLE, mode="r") as f:
        reader = csv.DictReader(f, fieldnames=CLIENT_SCHEMA)
        for row in reader:
            clients.append(row)


def _save_clients_to_storage():
    tmp_table_name = "{}.tmp".format(CLIENT_TABLE)
    with open(tmp_table_name, mode="w") as f:
        writer = csv.DictWriter(f, fieldnames=CLIENT_SCHEMA)
        writer.writerows(clients)
        os.remove(CLIENT_TABLE)
        os.rename(tmp_table_name, CLIENT_TABLE)


def create_client(client):

    if client not in clients:
        clients.append(client)
    else:
        print("Client alrady is in the client\s list")


def list_clients():
    """FUNCTION FOR DISPLAY CLIENTS"""
    # PARA ACCEDER A ESTA DOCUMENTACION DE LA FUNCION -DOCSTRINGS- EN CONSOLA help(list_clients)
    print("uid |  name  | company  | email  | position ")
    print("*" * 50)
    for idx, client in enumerate(clients):
        print(
            "{uid} | {name} | {company} | {email} | {position}".format(
                uid=idx,
                name=client["name"],
                company=client["company"],
                email=client["email"],
                position=client["position"],
            )
        )


def update_client(client_id, updated_client):
    global clients

    if len(clients) - 1 >= client_id:
        clients[client_id] = updated_client
    else:
        print("Client is not in clients list.")


def delete_clients(client):
    found = None

    for i in range(0, len(clients)):
        if client["name"] == clients[i]["name"]:
            del clients[i]
            found = True
            break

    if not found:
        print("Client is not in clients list.")


def search_client(client_name):
    for client in clients:
        if client["name"] != client_name:
            continue
        else:
            return True


def _get_client_field(field_name, message="What is the client {}? :"):
    field = None

    while not field:
        field = input(message.format(field_name))
        # field = input('What is the client {}?: '.format(field_name))

    return field


def _get_client_from_user():
    client = {
        "name": _get_client_field("name"),
        "company": _get_client_field("company"),
        "email": _get_client_field("email"),
        "position": _get_client_field("position"),
    }

    return client


def _print_welcome():
    print("WELCOME TO PLATZI VENTAS")
    print("*" * 50)
    print("What would you like todo today?")
    print("[C] Create client")
    print("[L] List client")
    print("[D] Delete client")
    print("[U] Update client")
    print("[S] Search client")
    print("[exit] EXIT")


if __name__ == "__main__":
    _initialize_clients_from_storage()
    _print_welcome()

    # SECUENCIA[COMIENZO:FINAL:PASOS]
    command = input()  # python3
    # command = raw_input()  # python 2
    command = command.upper()

    if command == "C":
        client = _get_client_from_user()
        create_client(client)
        # list_clients()
    elif command == "L":
        list_clients()
    elif command == "S":
        # client_name = _get_client_name()
        client_name = _get_client_field("name")
        found = search_client(client_name)

        if found:
            print("The client is in the client's list")
        else:
            print("The client: {} is not in the client's list".format(client_name))
    elif command == "D":
        # client = _get_client_data()
        # client_name = _get_client_name()
        client = {
            "name": _get_client_field("name"),
            # 'company': _get_client_field('company'),
            # 'email': _get_client_field('email'),
            # 'position': _get_client_field('position'),
        }
        delete_clients(client)
        # list_clients()
    elif command == "U":
        client_id = int(_get_client_field("id"))
        updated_client = _get_client_from_user()

        update_client(client_id, updated_client)

        # list_clients()
    else:
        print("Invalid command")

    _save_clients_to_storage()

# help(str) SE USA PARA SABER TODAS LAS OPCIONES QUE PODEMOS USAR CON LOS STRINGS

# ITERATORS AND GENERATOR

# def fibonacci(max):
#    a, b = 0, 1
#    while a < max:
#        yield a
#        a, b = b, a+b

# fib1 = fibonacci(20)
# fib_nums = [num for num in fib1]
# ...
# double_fib_nums = [num * 2 for num in fib1] # NO VA A FUNCIONAR
# double_fib_nums = [num * 2 for num in fibonacci(30)] # SÍ FUNCIONA
