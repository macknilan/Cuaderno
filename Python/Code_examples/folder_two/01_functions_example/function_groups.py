from dataclasses import dataclass
from typing import Callable, Iterable


@dataclass
class Customer:
    name: str
    age: int


class PaymentProcessor:
    def process_payment(self, amount: int, customer: Customer) -> None:
        print(f"Processing payment of {amount} for {customer.name}.")

    def refund_payment(self, amount: int, customer: Customer) -> None:
        print(f"Refunding payment of {amount} for {customer.name}.")


def process_payment_paypal(amount: int, customer: Customer) -> None:
    print(f"Processing payment of {amount} for {customer.name} using PayPal.")


def process_payment_stripe(amount: int, customer: Customer) -> None:
    print(f"Processing payment of {amount} for {customer.name} using Stripe.")


# Payment post-processing functions


def send_email_to_support(amount: int, customer: Customer) -> None:
    print(f"Sending email to team about payment of {amount} by {customer.name}.")


def store_analytics(amount: int, customer: Customer) -> None:
    print(f"Storing analytics about payment of {amount} by {customer.name}.")


def update_stock_levels(amount: int, customer: Customer) -> None:
    print(f"Updating stock levels for payment of {amount} by {customer.name}.")


def subscribe_to_newsletter(_: int, customer: Customer) -> None:
    print(f"Subscribing {customer.name} to newsletter.")


PostProcessingFunction = Callable[[int, Customer], None]
PAYMENT_POST_PROCESSORS_LIST = [
    send_email_to_support,
    store_analytics,
    update_stock_levels,
    subscribe_to_newsletter,
]
PAYMENT_POST_PROCESSORS_SET = {
    send_email_to_support,
    store_analytics,
    update_stock_levels,
    subscribe_to_newsletter,
}
PAYMENT_POST_PROCESSORS_TUPLE = (
    send_email_to_support,
    store_analytics,
    update_stock_levels,
    subscribe_to_newsletter,
)


def handle_payment_post_processors(
    amount: int, customer: Customer, post_processors: Iterable[PostProcessingFunction]
) -> None:
    for post_processor in post_processors:
        post_processor(amount, customer)


def main() -> None:
    alice = Customer("Alice", 25)
    processor = PaymentProcessor()
    processor.process_payment(100, alice)
    handle_payment_post_processors(100, alice, PAYMENT_POST_PROCESSORS_TUPLE)


if __name__ == "__main__":
    main()
