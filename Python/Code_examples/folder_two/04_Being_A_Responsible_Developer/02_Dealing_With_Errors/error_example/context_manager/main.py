import sqlite3
from dataclasses import dataclass
from datetime import datetime
from typing import Any


class SQLite:
    def __init__(self, file="application.db"):
        self.file = file

    def __enter__(self):
        self.conn = sqlite3.connect(self.file)
        return self.conn.cursor()

    def __exit__(self, type, value, traceback):
        print("Closing the connection")
        self.conn.close()


@dataclass
class NotFoundError(Exception):
    id: str


@dataclass
class NotAuthorizedError(Exception):
    id: str


@dataclass
class Blog:
    id: str
    published: datetime
    title: str
    content: str
    public: bool


def blog_lst_to_json(item: list[Any]) -> Blog:
    return Blog(
        id=item[0],
        published=item[1],
        title=item[2],
        content=item[3],
        public=bool(item[4]),
    )
    # return Blog(*item)


def fetch_blog(blog_id: str):
    with SQLite("application.db") as cur:

        # execute the query and fetch the data
        cur.execute("SELECT * FROM blogs where id=?", [blog_id])
        result = cur.fetchone()

        # return the result or raise an error
        if result is None:
            raise NotFoundError(blog_id)

        blog = blog_lst_to_json(result)
        if not blog.public:
            raise NotAuthorizedError(blog_id)
        return blog


def main() -> None:
    first_blog = fetch_blog("first-blog")
    private_blog = fetch_blog("private-blog")
    print(first_blog)
    print(private_blog)


if __name__ == "__main__":
    main()
