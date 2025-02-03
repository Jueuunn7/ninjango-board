from ninja_extra import NinjaExtraAPI

from board.presentation.controller import BoardController

api = NinjaExtraAPI()

api.register_controllers(BoardController)