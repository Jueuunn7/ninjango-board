from ninja_extra import NinjaExtraAPI

from board.presentation.controller import BoardController
from comment.presentation.controller import CommentController

api = NinjaExtraAPI()

api.register_controllers(BoardController)
api.register_controllers(CommentController)