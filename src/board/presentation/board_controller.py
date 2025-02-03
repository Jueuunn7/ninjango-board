from ninja_extra import api_controller, http_get
from typing import List
from injector import inject

from ..service.board_service import BoardService
from .board_schema import BoardOut


@api_controller('/board')
class BoardController:
    @inject
    def __init__(self, board_service: BoardService):
        self.board_service = board_service

    @http_get('', response=List[BoardOut])
    def get_all_boards(self):
        return self.board_service.get_all_boards()