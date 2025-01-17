# This file was generated by liblab | https://liblab.com/

from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models


class CarriersService(BaseService):

    @cast_models
    def carriers(self, x_api_key: str = None):
        """/carriers

        :param x_api_key: x_api_key, defaults to None
        :type x_api_key: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        Validator(str).is_optional().validate(x_api_key)

        serialized_request = (
            Serializer(
                f"{self.base_url}/apiservices/v3/flights/carriers",
                self.get_default_headers(),
            )
            .add_header("x-api-key", x_api_key)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return response
