from dataclasses import dataclass


@dataclass
class Item:
    name: str
    weight: float


def main() -> None:

    inventory = [
        Item("laptop", 1.5),
        Item("phone", 0.5),
        Item("book", 1.0),
        Item("camera", 1.0),
        Item("headphones", 0.5),
        Item("charger", 0.5),
    ]

    inventory_iterator = iter(inventory)

    print(next(inventory_iterator))
    print(next(inventory_iterator))
    print(next(inventory_iterator))
    print(next(inventory_iterator))
    print(next(inventory_iterator))
    print(next(inventory_iterator))
    # print(next(inventory_iterator))  # this raises a StopIteration exception

    # alternatively, we can use a for loop
    for item in inventory:
        print(item.weight)

    # a for loop creates an iterator object and executes the next() method for each iteration
    # behind the scenes, the for loop is equivalent to the following code:
    inventory_iterator = iter(inventory)
    while True:
        try:
            item = next(inventory_iterator)
        except StopIteration:
            break
        else:
            print(item.weight)

    # you can also call iter with a sentinel value
    # this is useful when you want to iterate over a stream of data
    # for example, you can read a file line by line
    # the sentinel value is a value that indicates the end of the stream
    # in this case, the sentinel value is an empty string
    with open("countries.txt") as f:
        for line in iter(f.readline, ""):
            print(line, end="")


if __name__ == "__main__":
    main()
