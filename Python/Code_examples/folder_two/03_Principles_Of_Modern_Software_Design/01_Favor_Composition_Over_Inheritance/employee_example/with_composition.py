"""
Very advanced Employee management system.
"""
from dataclasses import dataclass, field
from typing import Protocol


class PaymentSource(Protocol):
    def compute_pay(self) -> int:
        ...


@dataclass
class DealBasedCommission:

    commission: int = 10000
    deals_landed: int = 0

    def compute_pay(self) -> int:
        return self.commission * self.deals_landed


@dataclass
class HourlyContract:

    hourly_rate: int
    hours_worked: float = 0.0
    employer_cost: int = 100000

    def compute_pay(self) -> int:
        return int(self.hourly_rate * self.hours_worked + self.employer_cost)


@dataclass
class SalariedContract:

    monthly_salary: int
    percentage: float = 1

    def compute_pay(self) -> int:
        return int(self.monthly_salary * self.percentage)


@dataclass
class Employee:

    name: str
    id: int
    payment_sources: list[PaymentSource] = field(default_factory=list)

    def add_payment_source(self, payment_source: PaymentSource):
        self.payment_sources.append(payment_source)

    def compute_pay(self) -> int:
        return sum(source.compute_pay() for source in self.payment_sources)


def main() -> None:

    henry_contract = HourlyContract(hourly_rate=5000, hours_worked=100)
    henry = Employee(name="Henry", id=12346, payment_sources=[henry_contract])
    print(f"{henry.name} earned ${(henry.compute_pay() / 100):.2f}.")

    sarah_contract = SalariedContract(monthly_salary=500000)
    sarah_commission = DealBasedCommission(deals_landed=10)
    sarah = Employee(
        name="Sarah", id=47832, payment_sources=[sarah_contract, sarah_commission]
    )
    print(f"{sarah.name} earned ${(sarah.compute_pay() / 100):.2f}.")


if __name__ == "__main__":
    main()
