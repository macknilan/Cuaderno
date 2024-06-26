from pos.authorization import authorize_google
from pos.order import Order
from pos.payment import PaypalPaymentProcessor


def main():
    order = Order()
    order.add_item("Keyboard", 1, 5000)
    order.add_item("SSD", 1, 15000)
    order.add_item("USB cable", 2, 500)

    print(f"The total price is: ${(order.total_price / 100):.2f}.")
    processor = PaypalPaymentProcessor("hi@arjancodes.com")
    processor.pay(order, authorize_google)


if __name__ == "__main__":
    main()
