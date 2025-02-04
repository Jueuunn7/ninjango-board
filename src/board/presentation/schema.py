from ninja import Schema


class BoardOut(Schema):
    id: int
    title: str
    content: str


class BoardIn(Schema):
    title: str
    content: str