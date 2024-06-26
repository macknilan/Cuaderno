import random
import string
from enum import Enum, auto


def generate_vehicle_license() -> str:
    """Helper method for generating a vehicle license number."""

    digit_part = "".join(random.choices(string.digits, k=2))
    letter_part_1 = "".join(random.choices(string.ascii_uppercase, k=2))
    letter_part_2 = "".join(random.choices(string.ascii_uppercase, k=2))
    return f"{letter_part_1}-{digit_part}-{letter_part_2}"


class Accessory(Enum):
    AIRCO = auto()
    CRUISECONTROL = auto()
    NAVIGATION = auto()
    OPENROOF = auto()
    BATHTUB = auto()
    MINIBAR = auto()


class FuelType(Enum):
    PETROL = auto()
    DIESEL = auto()
    ELECTRIC = auto()


class Vehicle:
    def __init__(
        self,
        brand: str,
        model: str,
        color: str,
        license_plate: str,
        fuel_type: FuelType = FuelType.ELECTRIC,
        accessories: list[Accessory] = [],
    ) -> None:
        self.brand = brand
        self.model = model
        self.color = color
        self.fuel_type = fuel_type
        self.license_plate = license_plate
        self.accessories = accessories


def main() -> None:
    """
    Create some vehicles and print their details.
    """

    tesla = Vehicle(
        brand="Tesla",
        model="Model 3",
        color="black",
        license_plate=generate_vehicle_license(),
        accessories=[
            Accessory.AIRCO,
            Accessory.MINIBAR,
            Accessory.NAVIGATION,
            Accessory.CRUISECONTROL,
        ],
    )
    volkswagen = Vehicle(
        brand="Volkswagen",
        model="ID3",
        color="white",
        license_plate=generate_vehicle_license(),
        accessories=[Accessory.AIRCO, Accessory.NAVIGATION],
    )
    bmw = Vehicle(
        brand="BMW",
        model="520e",
        color="blue",
        license_plate=generate_vehicle_license(),
        fuel_type=FuelType.PETROL,
        accessories=[Accessory.NAVIGATION, Accessory.CRUISECONTROL],
    )

    print(tesla)
    print(volkswagen)
    print(bmw)


if __name__ == "__main__":
    main()
