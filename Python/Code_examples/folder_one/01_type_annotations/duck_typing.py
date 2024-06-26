my_str: str = "Hello World"
my_list: list[int] = [34, 54, 65, 78]
my_dict: dict[str, int] = {"one": 123, "two": 456, "three": 789}

len(my_str)  # 11
len(my_list)  # 4
len(my_dict)  # 3


class Book:
    def __init__(self, author: str, title: str, pages: int) -> None:
        self.author = author
        self.title = title
        self.pages = pages

    def __len__(self) -> int:
        return self.pages


print(len(Book("Robert Martin", "Clean Code", 464)))
