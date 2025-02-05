from django.db import transaction
from typing import List
from injector import inject

from comment.presentation.schema import CommentOut
from ..domain.repository import BoardRepository
from ..domain.models import Board
from ..presentation.schema import BoardOut
from ..exceptions import BoardNotFoundException


class BoardService:
    @inject
    def __init__(self, board_repository: BoardRepository):
        self.board_repository = board_repository

    def get_all_boards(self):
        return [
            BoardOut(
                id=b.id,
                title=b.title,
                content=b.content,
                comments=[
                    CommentOut(
                        content=c.content
                    )
                    for c in b.comments.all()
                ]
            )
            for b in self.board_repository.find_all()
        ]
    
    def get_board_by_id(self, id):
        return self.board_repository.find_by_id(id)\
            .NotFound(BoardNotFoundException)

    @transaction.atomic
    def create_board(self, board_data):
        return self.board_repository.create(
            Board(
                title=board_data.title,
                content=board_data.content
            )
        )
    
    @transaction.atomic
    def update_board(self, id, board_data):
        board = self.board_repository.find_by_id(id)\
            .NotFound(BoardNotFoundException)

        board.title = board_data.title
        board.content = board_data.content

        board.save()

        return board
    
    @transaction.atomic
    def delete_board(self, id):
        board = self.board_repository.find_by_id(id)\
            .NotFound(BoardNotFoundException)
        board.delete()
        