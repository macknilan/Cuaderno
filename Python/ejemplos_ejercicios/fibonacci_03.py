fibonacci_cache = {}


def fibonacci(n):
    """Si el valor se encuentra en cache se retorna."""

    if n in fibonacci_cache:
        return fibonacci_cache[n]

    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonacci(n - 1) + fibonacci(n - 2)
    # Se hace cahce del valor y se retorna
    fibonacci_cache[n] = value
    return value


for n in range(1, 11):
    print(f"{n} : {fibonacci(n)}")
