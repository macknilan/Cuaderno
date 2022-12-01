"""
Script para determinar el tiempo que tarda una suma con decorador.
"""
import time


def timer_track(function):
    def wrapper(*args, **kwargs):
        print(f"*args - {args} / **kwargs - {kwargs}")
        start = time.time()
        print(f"start --> {start}")

        function(*args, **kwargs)
        print(f"{ time.time() - start }")

    return wrapper


@timer_track
def example():
    sum = 0
    for _ in range(1_000_000_000):
        sum += 1


example()
