from rest_framework.renderers import JSONRenderer
from rest_framework import status


class CustomRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        # Get the response object and status code
        response = renderer_context.get("response", None)  # type:ignore
        status_code = response.status_code if response else status.HTTP_200_OK

        # Default message based on status code
        default_messages = {
            status.HTTP_200_OK: "Success",
            status.HTTP_201_CREATED: "Resource created successfully",
            status.HTTP_400_BAD_REQUEST: "Invalid request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
            status.HTTP_403_FORBIDDEN: "Forbidden",
            status.HTTP_404_NOT_FOUND: "Not found",
            status.HTTP_500_INTERNAL_SERVER_ERROR: "Server error",
        }
        message = default_messages.get(status_code, "Unknown status")

        # If data is already in BaseResponse format, use it as is
        if (
            isinstance(data, dict)
            and "status" in data
            and "message" in data
            and "data" in data
        ):
            wrapped_data = data
        else:
            # Wrap the data in the custom format
            wrapped_data = {
                "status": status_code,
                "message": message,
                "data": data if data is not None else {},
            }

        # Render the wrapped data as JSON
        return super().render(wrapped_data, accepted_media_type, renderer_context)
