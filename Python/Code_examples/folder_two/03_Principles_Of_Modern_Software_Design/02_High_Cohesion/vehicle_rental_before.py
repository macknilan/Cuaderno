def main():
    print("Vehicle Rental before")

    price_per_km_vw = 30
    price_per_km_bmw = 35
    price_per_km_ford = 25
    price_per_day_vw = 6000
    price_per_day_bmw = 8500
    price_per_day_ford = 12000

    vehicle_type = ""
    while vehicle_type != "vw" and vehicle_type != "bmw" and vehicle_type != "ford":
        vehicle_type = input(
            "What type of vehicle would you like to rent (choose vw, bmw, or ford)? "
        )

    days = 0
    while days < 1:
        days_str = input(
            "How many days would you like to rent the vehicle? (enter a positive number) "
        )
        try:
            days = int(days_str)
        except ValueError:
            print("Invalid input. Please enter a number.")

    km = 0
    while km < 1:
        km_str = input(
            "How many kilometers would you like to drive (enter a positive number)? "
        )
        try:
            km = int(km_str)
        except ValueError:
            print("Invalid input. Please enter a number.")

    # subtract the base number of kms
    km = max(km - 100, 0)

    # compute the final rental price
    rental_price = 0
    if vehicle_type == "vw":
        rental_price = price_per_km_vw * km + price_per_day_vw * days
    elif vehicle_type == "bmw":
        rental_price = price_per_km_bmw * km + price_per_day_bmw * days
    elif vehicle_type == "ford":
        rental_price = price_per_km_ford * km + price_per_day_ford * days
    else:
        print("Error")

    # print the result
    print(f"The total price of the rental is ${(rental_price / 100):.2f}")


if __name__ == "__main__":
    main()
