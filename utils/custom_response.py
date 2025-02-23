from rest_framework.response import Response


class BaseResponse(Response):
    """
    Custom Response class to enforce a standardized response structure.
    """

    def __init__(
        self,
        data=None,
        message="Success",
        success=True,
        status_code=200,
        status=None,
        headers=None,
    ):
        response_data = {
            "status_code": status_code,
            "success": success,
            "message": message,
            "data": data if data is not None else {},
        }
        super().__init__(
            response_data, status=status if status else status_code, headers=headers
        )
