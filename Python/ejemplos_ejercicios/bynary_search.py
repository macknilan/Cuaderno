# -*- coding: utf-8 -*-
"""binary_search.py"""


def str_2_list(disorder_list):
    split_list = map(int, disorder_list.split(" "))
    order_list = sorted(split_list)

    return order_list


def bynary_search(order_numbers, number_to_find, low, high):
    if low > high:
        return False

    mid = (low + high) / 2

    if order_numbers[mid] == number_to_find:
        return True
    elif order_numbers[mid] > number_to_find:
        return bynary_search(order_numbers, number_to_find, low, mid - 1)
    else:
        return bynary_search(order_numbers, number_to_find, mid + 1, high)


if __name__ == "__main__":
    disorder_list = str(
        input(
            "Escribe una lista de numeros --AL MENOS DIEZ NUMEROS-- separados por <<ESPACIOS>>: "
        )
    )
    order_numbers = str_2_list(disorder_list)
    number_to_find = int(input("Ingresa un número a buscar: "))

    result = bynary_search(order_numbers, number_to_find, 0, len(order_numbers) - 1)

    if result is True:
        print("El numero sí esta en la lista")
    else:
        print("El numero NO esta en la lista")
