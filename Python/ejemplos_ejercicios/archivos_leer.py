def read():
    numbers = []
    with open("./numbers.txt", "r") as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)


def write():
    names = ["Rodolfo", "Gregorio", "Marta", "Susana", "Jose"]
    with open("./names.txt", "w") as f:
        for name in names:
            f.write(name)
            f.write("\n")


def run():
    write()


if __name__ == "__main__":
    run()
