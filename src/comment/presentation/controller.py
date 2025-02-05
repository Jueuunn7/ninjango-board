from ninja_extra.controllers import api_controller
from injector import inject


from ..service.service import CommentService


@api_controller('comment')
class CommentController:
    @inject
    def __init__(self, comment_service: CommentService):
        self.comment_service = comment_service
