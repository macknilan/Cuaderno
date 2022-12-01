def fibonacci(n):
    if n == 0 or n == 1:
        # print(f"return", {n})
        return 1

    print(
        f"{fibonacci(n - 1)} {fibonacci(n - 2)} {fibonacci(n - 1) + fibonacci(n - 2)}"
    )
    # print(f"{fibonacci(n - 1) + fibonacci(n - 2)}")
    return fibonacci(n - 1) + fibonacci(n - 2)


n = int(input("Escribe un numero entero: "))

print(f"El numero fibonacci de {n} es {fibonacci(n)}")
