import sqlite3
from dataclasses import dataclass
from datetime import datetime
from typing import Any


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
    # connect to the database
    con = sqlite3.connect("application.db")
    cur = con.cursor()

    # execute the query and fetch the data
    cur.execute("SELECT * FROM blogs where id=?", [blog_id])
    result = cur.fetchone()

    # close the database
    con.close()

    return blog_lst_to_json(result)


def main() -> None:
    first_blog = fetch_blog("first-blog")
    private_blog = fetch_blog("private-blog")
    print(first_blog)
    print(private_blog)


if __name__ == "__main__":
    main()
