from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Protocol


class Pricing(Protocol):
    def get_total_price(self) -> int:
        ...


class PricePerDay:
    price_per_day: int = 100_00
    nr_days: int = 1

    def get_total_price(self) -> int:
        return self.price_per_day * self.nr_days


class PricePerMonth:
    price_per_month: int = 500_00
    nr_months: int = 1

    def get_total_price(self) -> int:
        return self.price_per_month * self.nr_months


class PricePerKm:
    price_per_km: int = 30
    nr_kms: int = 100

    def get_total_price(self) -> int:
        return self.price_per_km * self.nr_kms


class FuelType(Enum):
    PETROL = auto()
    DIESEL = auto()
    ELECTRIC = auto()


class TruckCabStyle(Enum):
    REGULAR = auto()
    EXTENDED = auto()
    CREW = auto()


@dataclass
class Vehicle:
    brand: str
    model: str
    color: str
    fuel_type: FuelType
    license_plate: str
    reserved: bool = False
    pricing: list[Pricing] = field(default_factory=list)


@dataclass
class Car(Vehicle):
    number_of_seats: int = 5
    storage_capacity_litres: int = 40


@dataclass
class Truck(Vehicle):
    cab_style: TruckCabStyle = TruckCabStyle.REGULAR


@dataclass
class Trailer:
    brand: str
    model: str
    capacity_m3: int
    reserved: bool = False
    pricing: list[Pricing] = field(default_factory=list)


def main():
    pass


if __name__ == "__main__":
    main()
