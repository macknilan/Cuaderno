VEHICLE_DATA = {
    "vw": {"price_per_km": 30, "price_per_day": 6000},
    "bmw": {"price_per_km": 35, "price_per_day": 8500},
    "ford": {"price_per_km": 25, "price_per_day": 12000},
}


def read_vehicle_type() -> str:
    """Reads the vehicle type from the user."""
    vehicle_type = ""
    while vehicle_type not in VEHICLE_DATA:
        vehicle_type = input(
            f"What type of vehicle would you like to rent ({', '.join(VEHICLE_DATA)})? "
        )
    return vehicle_type


def read_rent_days() -> int:
    """Reads the number of days from the user."""
    days = 0
    while days < 1:
        days_str = input(
            "How many days would you like to rent the vehicle? (enter a positive number) "
        )
        try:
            days = int(days_str)
        except ValueError:
            print("Invalid input. Please enter a number.")
    return days


def read_kms_to_drive() -> int:
    """Reads the number of kilometers to drive from the user."""
    km = 0
    while km < 1:
        km_str = input(
            "How many kilometers would you like to drive (enter a positive number)? "
        )
        try:
            km = int(km_str)
        except ValueError:
            print("Invalid input. Please enter a number.")
    return km


def compute_rental_cost(vehicle_type: str, days: int, km: int) -> int:
    """Computes the rental cost for a vehicle."""
    vehicle_data = VEHICLE_DATA[vehicle_type]
    price_per_km = vehicle_data["price_per_km"]
    price_per_day = vehicle_data["price_per_day"]
    paid_kms = max(km - 100, 0)
    return price_per_km * paid_kms + price_per_day * days


def main():
    print("Vehicle Rental before")

    vehicle_type = read_vehicle_type()

    days = read_rent_days()

    km = read_kms_to_drive()

    # compute the final rental price
    rental_price = compute_rental_cost(vehicle_type, days, km)

    # print the result
    print(f"The total price of the rental is ${(rental_price / 100):.2f}")


if __name__ == "__main__":
    main()
