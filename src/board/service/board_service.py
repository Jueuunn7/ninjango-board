from typing import List
from injector import inject

from ..domain.board_repository import BoardRepository
from ..presentation.board_schema import BoardOut


class BoardService:
    @inject
    def __init__(self, board_repository: BoardRepository):
        self.board_repository = board_repository

    def get_all_boards(self) -> List[BoardOut]:
        return [
            BoardOut(
                id=b.id,
                title=b.title,
                content=b.content,
            )
            for b in self.board_repository.get_all()
        ]
