
# https://www.youtube.com/watch?v=vBH6GRJ1REM
# https://realpython.com/python-data-classes/
# https://github.com/mCodingLLC/VideosSampleCode

import dataclasses
import inspect
from dataclasses import dataclass, field
from typing import List
from pprint import pprint

@dataclass()
class Comment:
    id: int
    text: str
    replies: List[int] = field(default_factory=list)

    def __str__(self):
        return f'{self.id}, ({self.text}, {self.replies})'


def main():
    comment = Comment(1, "This is a comment", [1, 2, 3])
    # print(f"comment --> {comment}")
    # Comment(id=1, text='This is a comment')
    
    print(dataclasses.astuple(comment))
    # (1, 'This is a comment')
    print(dataclasses.asdict(comment))
    # {'id': 1, 'text': 'This is a comment'}

    pprint(inspect.getmembers(Comment, inspect.isfunction))


if __name__ == '__main__':
    main()

