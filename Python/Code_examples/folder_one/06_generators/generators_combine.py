import itertools
from typing import Generator, Iterable


def power_generator(numbers: Iterable[int]) -> Generator[int, None, None]:
    for i in numbers:
        yield 2**i


def partial_sums(numbers: Iterable[int]) -> Generator[int, None, None]:
    total = 0
    for i in numbers:
        total += i
        yield total


def main() -> None:
    print(list(partial_sums(power_generator(range(10)))))
    chained = itertools.chain(power_generator(range(10)), partial_sums(range(10)))
    print(list(chained))


if __name__ == "__main__":
    main()
