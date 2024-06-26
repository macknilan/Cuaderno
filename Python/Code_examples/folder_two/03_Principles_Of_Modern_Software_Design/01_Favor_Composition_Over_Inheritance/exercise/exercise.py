from dataclasses import dataclass
from enum import Enum, auto


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
    reserved: bool


@dataclass
class VehiclePerDay(Vehicle):
    price_per_km: int
    price_per_day: int


@dataclass
class VehiclePerMonth(Vehicle):
    price_per_month: int


@dataclass
class CarPerDay(VehiclePerDay):
    number_of_seats: int
    storage_capacity_litres: int


@dataclass
class CarPerMonth(VehiclePerMonth):
    number_of_seats: int
    storage_capacity_litres: int


@dataclass
class Truck(Vehicle):
    cab_style: TruckCabStyle


@dataclass
class Trailer:
    brand: str
    model: str
    capacity_m3: int
    price_per_month: int
    reserved: bool


def main():
    pass


if __name__ == "__main__":
    main()
