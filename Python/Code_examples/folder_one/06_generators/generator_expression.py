def main() -> None:
    powers = (2**i for i in range(10))
    for power in powers:
        print(power)

    # you can also use generator expressions as function arguments
    print(sum(2**i for i in range(10)))


if __name__ == "__main__":
    main()
