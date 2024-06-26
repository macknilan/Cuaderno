CUSTOMERS = {
    "Alice": {"phone": "2341", "credit_card": "2341"},
    "Bob": {"phone": "9102", "credit_card": "5342"},
}


def pure_function(x: int, y: int) -> int:
    return x + y


def side_effect_function() -> None:
    CUSTOMERS["Alice"]["phone"] = "1234"


def main() -> None:
    print(pure_function(1, 2))
    side_effect_function()
    print(CUSTOMERS)


if __name__ == "__main__":
    main()
