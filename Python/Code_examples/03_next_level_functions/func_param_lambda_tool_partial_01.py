
from typing import Tuple

import math
import functools


def greet(name, message):
    return f"{message}, {name}!"


greeter = functools.partial(greet, message="Hello")
print(greeter("Alice"))  # Output: Hello, Alice!


def greet_with_exclamation(name):
    return greet(name, message="Hello!")


greeter_with_exclamation = functools.partial(greet, message="Hello!")
print(greeter_with_exclamation("Bob"))  # Output: Hello, Bob!


def subtract(x, y):
    return x - y


subtract_from_five = functools.partial(subtract, y=5)
print(subtract_from_five(10))  # Output: 5


def call_with_positional_and_keyword_arguments(func, x, **kwargs):
    return func(x, **kwargs)


call_with_positional_and_keyword_arguments = functools.partial(call_with_positional_and_keyword_arguments, subtract)
print(call_with_positional_and_keyword_arguments(10, y=2))  # Output: 8


def euclidean_distance(point1: Tuple[int, int], point2: Tuple[int, int]) -> float:
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


zero_euclid = functools.partial(euclidean_distance, (0, 0))
point = (1, 1)
print(zero_euclid(point))


