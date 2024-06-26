from typing import Callable

from pos.authorization import authorize_google, authorize_sms
from pos.order import Order
from pos.payment import (
    AuthorizeFunction,
    CreditPaymentProcessor,
    DebitPaymentProcessor,
    PaymentProcessor,
    PaypalPaymentProcessor,
)


def create_credit_payment_processor() -> PaymentProcessor:
    security_code = input("Enter the security code: ")
    return CreditPaymentProcessor(security_code)


def create_debit_payment_processor() -> PaymentProcessor:
    return DebitPaymentProcessor()


def create_paypal_payment_processor() -> PaymentProcessor:
    email_address = input("Enter your email address: ")
    return PaypalPaymentProcessor(email_address)


PAYMENT_PROCESSORS: dict[str, Callable[[], PaymentProcessor]] = {
    "credit": create_credit_payment_processor,
    "debit": create_debit_payment_processor,
    "paypal": create_paypal_payment_processor,
}

AUTHORIZERS: dict[str, AuthorizeFunction] = {
    "google": authorize_google,
    "sms": authorize_sms,
}


def read_choice(question: str, choices: list[str]) -> str:
    choice = ""
    while choice not in choices:
        choice = input(f"{question} ({', '.join(choices)})? ")
    return choice


def read_payment_choice() -> PaymentProcessor:
    payment_choice = read_choice(
        "How would you like to pay?", ["paypal", "credit", "debit"]
    )
    return PAYMENT_PROCESSORS[payment_choice]()


def read_authorizer() -> AuthorizeFunction:
    auth_choice = read_choice("Choose your authentication method", ["google", "sms"])
    return AUTHORIZERS[auth_choice]


def create_order():
    order = Order()
    order.add_item("Keyboard", 1, 5000)
    order.add_item("SSD", 1, 15000)
    order.add_item("USB cable", 2, 500)
    return order


def main():
    order = create_order()
    print(f"The total price is: ${(order.total_price / 100):.2f}.")

    # select the payment method
    payment_processor = read_payment_choice()

    # select the authentication method
    authorizer = read_authorizer()

    payment_processor.pay(order, authorizer)


if __name__ == "__main__":
    main()
