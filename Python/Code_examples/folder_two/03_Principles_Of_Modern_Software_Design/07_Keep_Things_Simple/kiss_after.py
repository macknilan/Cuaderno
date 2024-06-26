from dataclasses import dataclass
from enum import Enum, auto


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


class Order:
    def __init__(self):
        self.items: list[LineItem] = []
        self.status: PaymentStatus = PaymentStatus.OPEN
        self.fixed_discount: int = 0
        self.variable_discount: float = 0.0

    def add_item(self, item: LineItem) -> None:
        self.items.append(item)

    @property
    def total_price(self) -> int:
        sub_total = sum(item.total_price for item in self.items)
        discount = int(self.fixed_discount + self.variable_discount * sub_total)
        return sub_total - discount


def main() -> None:
    order = Order()
    order.add_item(LineItem("Keyboard", 1, 5000))
    order.add_item(LineItem("SSD", 1, 15000))
    order.add_item(LineItem("USB cable", 2, 500))
    order.variable_discount = 0.15
    order.fixed_discount = 1000

    print(f"The total price is: ${(order.total_price / 100):.2f}.")


if __name__ == "__main__":
    main()
