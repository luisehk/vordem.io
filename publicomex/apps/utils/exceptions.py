from rest_framework.exceptions import APIException


class ConstraintsError(APIException):
    status_code = 409
    default_detail = (
        'There was a problem running your query. '
        'Maybe an object with those values already existed?'
    )
    default_code = 'contraints_error'
