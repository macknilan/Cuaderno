from typing import Protocol


class Counter(Protocol):
    def increment(self) -> None:
        ...

    def decrement(self) -> None:
        pass


class MyCounter(Counter):
    def __init__(self, initial_count: int) -> None:
        self.count = initial_count

    def increment(self) -> None:
        self.count += 1

    def decrement(self) -> None:
        self.count -= 1


def main() -> None:
    counter = MyCounter(10)
    counter.increment()
    print(counter.count)  # 11
    counter.decrement()
    print(counter.count)  # 10


if __name__ == "__main__":
    main()
