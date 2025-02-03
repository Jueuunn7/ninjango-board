from typing import List

from ..models import Board


class BoardRepository:
    def get_all(self) -> List[Board]:
        return Board.objects.all()