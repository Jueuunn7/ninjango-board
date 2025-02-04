from typing import List

from ..models import Board
from core.decorator.repository import Repository
    

class BoardRepository:
    def find_all(self) -> List[Board]:
        return Board.objects.all()
    
    @Repository.notfound
    def find_by_id(self, id) -> Board:
        return Board.objects.filter(id=id).first()
    
    def create(self, board: Board) -> Board:
        return Board.objects.create(
            title=board.title, 
            content=board.content
        )
