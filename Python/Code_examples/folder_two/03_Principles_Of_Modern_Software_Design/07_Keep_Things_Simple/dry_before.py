def read_vehicle_type() -> str:
    vehicle_types = ["vw", "bmw", "tesla"]
    vehicle_type = ""
    while vehicle_type not in vehicle_types:
        vehicle_type = input(
            f"What type of vehicle would you like to rent ({', '.join(vehicle_types)})? "
        )
    return vehicle_type


def read_vehicle_color() -> str:
    vehicle_colors = ["black", "red", "blue"]
    vehicle_color = ""
    while vehicle_color not in vehicle_colors:
        vehicle_color = input(
            f"What color vehicle would you like to rent ({', '.join(vehicle_colors)})? "
        )
    return vehicle_color


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


def main():

    vehicle_type = read_vehicle_type()

    vehicle_color = read_vehicle_color()

    days = read_rent_days()

    kms = read_kms_to_drive()

    print(
        f"You rented a {vehicle_type} vehicle, color {vehicle_color}, for {days} days",
        f"and you're allowed to drive {kms} kilometers.",
    )


if __name__ == "__main__":
    main()
