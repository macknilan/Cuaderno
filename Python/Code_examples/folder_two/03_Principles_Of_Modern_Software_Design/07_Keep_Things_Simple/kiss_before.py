from dataclasses import dataclass
from enum import Enum, auto
from typing import Protocol


class PaymentStatus(Enum):
    """Payment status"""

    OPEN = auto()
    PAID = auto()


@dataclass
class LineItem:
    name: str
    quantity: int
    price: int

    @property
    def total_price(self) -> int:
        return self.quantity * self.price


class Discount(Protocol):
    def compute_discount(self, price: int) -> int:
        """Computes the discount, given a price."""


@dataclass
class FixedDiscount:
    discount: int = 0

    def compute_discount(self, price: int) -> int:
        return self.discount


@dataclass
class VariableDiscount:
    discount_percentage: float = 0

    def compute_discount(self, price: int) -> int:
        return int(self.discount_percentage * price)


class Order:
    def __init__(self):
        self.items: list[LineItem] = []
        self.status: PaymentStatus = PaymentStatus.OPEN
        self.discounts: list[Discount] = []

    def add_item(self, name: str, quantity: int, price: int) -> None:
        self.items.append(LineItem(name, quantity, price))

    def add_discount(self, discount: Discount) -> None:
        self.discounts.append(discount)

    @property
    def total_price(self) -> int:
        total = 0
        for item in self.items:
            total += item.total_price
        total_discount = 0
        for discount in self.discounts:
            total_discount += discount.compute_discount(total)
        return total - total_discount


def create_order(items: list[LineItem], discounts: list[Discount]):
    order = Order()
    for item in items:
        order.add_item(item.name, item.quantity, item.price)
    for discount in discounts:
        order.add_discount(discount)
    return order


def main() -> None:
    order = create_order(
        [
            LineItem("Keyboard", 1, 5000),
            LineItem("SSD", 1, 15000),
            LineItem("USB cable", 2, 500),
        ],
        [VariableDiscount(0.1), FixedDiscount(1000), VariableDiscount(0.05)],
    )
    print(f"The total price is: ${(order.total_price / 100):.2f}.")


if __name__ == "__main__":
    main()
