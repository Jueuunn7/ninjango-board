from ninja_extra.exceptions import APIException
from ninja_extra import status


class BoardNotFoundException(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = 'Board Not Found.'