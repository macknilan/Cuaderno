import random


def busqueda_lineal(lista, objetivo):
    contador_lineal = 0
    match = False
    for elemento in lista:  # O(n) Lineal
        contador_lineal += 1
        if elemento == objetivo:
            contador_lineal += 1
            match = True
            break

    return contador_lineal

def busqueda_binaria(lista, comienzo, final, objetivo, contador_binario=0):
    print(f"buscando {objetivo} entre {lista[comienzo]} y {lista[final - 1]}")
    contador_binario += 1
    if comienzo > final:
        return False

    medio = (comienzo + final) // 2

    if lista[medio] == objetivo:
        return contador_binario
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, medio + 1, final, objetivo, contador_binario=contador_binario)
    else:
        return busqueda_binaria(lista, comienzo, medio - 1, objetivo, contador_binario=contador_binario)


if __name__ == "__main__":
    tamano_de_lista = int(input("De que tamano es la lista? "))
    objetivo = int(input("Que numero quieres encontrar? "))

    lista = [random.randint(0, 100) for i in range(tamano_de_lista)]
    encontrado_busqueda_lineal = busqueda_lineal(lista, objetivo)

    lista = sorted([random.randint(0, 100) for i in range(tamano_de_lista)])
    encontrado_busqueda_binaria = busqueda_binaria(lista, 0, len(lista), objetivo)

    print(lista)
    print(f"Iteraciones en la busqueda lineal {encontrado_busqueda_lineal}")
    print(f"Iteraciones en la busqueda binaria {encontrado_busqueda_binaria}")

    print(
        f'El elemento {objetivo} {"esta" if encontrado_busqueda_lineal else "no esta"} en la lista'
    )
    print(
        f'El elemento {objetivo} {"esta" if encontrado_busqueda_binaria else "no esta"} en la lista'
    )
