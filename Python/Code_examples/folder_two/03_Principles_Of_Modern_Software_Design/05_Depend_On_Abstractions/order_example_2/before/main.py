from pos.order import Order
from pos.payment import PaymentProcessor


def main():
    order = Order()
    order.add_item("Keyboard", 1, 5000)
    order.add_item("SSD", 1, 15000)
    order.add_item("USB cable", 2, 500)

    print(f"The total price is: ${(order.total_price / 100):.2f}.")
    processor = PaymentProcessor("sms")
    processor.pay_credit(order, "123456")


if __name__ == "__main__":
    main()
