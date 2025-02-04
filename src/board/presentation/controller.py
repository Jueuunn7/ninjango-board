from ninja_extra import api_controller, http_get, http_post, http_put, http_delete
from typing import List
from injector import inject

from ..service.service import BoardService
from .schema import BoardOut, BoardIn


@api_controller('/board')
class BoardController:
    @inject
    def __init__(self, board_service: BoardService):
        self.board_service = board_service

    @http_get('', response=List[BoardOut])
    def get_all_boards(self):
        return 200, self.board_service.get_all_boards()
    
    @http_get('/{id}', response=BoardOut)
    def get_board_by_id(self, id):
        return 200, self.board_service.get_board_by_id(id)
    
    @http_post('', response=None)
    def create_board(self, board_data: BoardIn):
        self.board_service.create_board(board_data)
        return 201
    
    @http_put('/{id}', response=None)
    def update_board(self, id: int, board_data: BoardIn):
        self.board_service.update_board(id, board_data)
        return 200
    
    @http_delete('/{id}', response=None)
    def delete_board(self, id: int):
        self.board_service.delete_board(id)
        return 204