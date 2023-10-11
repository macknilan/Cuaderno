from typing import Protocol


class Shape(Protocol):
    def area(self) -> float:
        ...

    def perimeter(self) -> float:
        ...


class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return 3.14 * self.radius * self.radius

    def perimeter(self) -> float:
        return 2 * 3.14 * self.radius


def print_shape_info(shape: Shape):
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")


circle = Circle(10)
print_shape_info(circle)
