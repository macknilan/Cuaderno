import math
from dataclasses import dataclass
from datetime import datetime
from typing import Protocol


class Rentable(Protocol):
    def reserve(self, start_date: datetime, days: int):
        ...


class LicenseHolder(Protocol):
    def renew_license(self, new_license_date: datetime):
        ...


@dataclass
class Car:
    model: str
    reserved: bool = False

    def reserve(self, start_date: datetime, days: int):
        self.reserved = True
        print(f"Reserving car {self.model} for {days} days at date {start_date}.")


@dataclass
class Truck:
    model: str
    reserved: bool = False
    reserved_trailer: bool = False

    def reserve(self, start_date: datetime, days: int):
        months = math.ceil(days / 30)
        self.reserved = True
        self.reserved_trailer = True
        print(
            f"Reserving truck {self.model} for {months} month(s) at date {start_date}, including a trailer."
        )

    def renew_license(self, new_license_date: datetime):
        print(f"Renewing the license until {new_license_date}.")


def reserve_now(rentable: Rentable):
    rentable.reserve(datetime.now(), 1)


def renew_license(license_holder: LicenseHolder):
    license_holder.renew_license(datetime.now())


def main():
    car = Car("Ford")
    truck = Truck("DAF")
    reserve_now(car)
    reserve_now(truck)
    renew_license(truck)


if __name__ == "__main__":
    main()
