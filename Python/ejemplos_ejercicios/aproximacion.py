objetivo = int(input("Escoge un numero: "))
epsilon = 0.01
paso = epsilon**2
respuesta = 0.0

while abs(respuesta**2 - objetivo) >= epsilon and respuesta**2 <= objetivo:
    print(abs(respuesta**2 - objetivo), epsilon, respuesta)
    respuesta += paso

if abs(respuesta**2 - objetivo) >= epsilon:
    print(f"No se encontró la raíz cuadrada {objetivo}")
else:
    print(f"La raíz cuadrada de {objetivo} es {respuesta}")
