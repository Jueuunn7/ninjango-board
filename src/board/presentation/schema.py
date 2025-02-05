from ninja import Schema
from typing import List

from comment.presentation.schema import CommentOut


class BoardOut(Schema):
    id: int
    title: str
    content: str
    comments: List[CommentOut]


class BoardIn(Schema):
    title: str
    content: str