from rest_framework import permissions
from .permissions import IsStaffEditorPermission
from rest_framework.response import Response


class StaffEditorPermissionMixin:
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]


class UserQuerysetMixin:
    user_field = "user"

    def get_queryset(self, *args, **kwargs):
        lookup_data = {}
        lookup_data[self.user_field] = self.request.user  # type:ignore
        qs = super().get_queryset(*args, **kwargs)  # type:ignore
        return qs.filter(**lookup_data)


class ResponseWrapperMixin:
    def finalize_response(self, request, response, *args, **kwargs):
        if isinstance(response, Response):
            message = getattr(self, "message", None)
            data = response.data
            if response.status_code >= 400:
                data = None
                if message is None and isinstance(response.data, dict):
                    message = response.data.get("detail", "Error")
                else:
                    message = "Success" if response.status_code < 400 else "Error"

            wrapped_data = {
                "status": response.status_code,
                "message": message,
                "data": data,
            }
            response.data = wrapped_data
        return super().finalize_response(  # type:ignore
            request, response, *args, **kwargs
        )
