from django.contrib.auth.mixins import AccessMixin

class MiembroRequiredMixin(AccessMixin):
    """Verify that the current user is authenticated."""

    # def dispatch(self, request, *args, **kwargs):
    #     if not request.user.is_miembro:
    #         return self.handle_no_permission()
    #     return super().dispatch(request, *args, **kwargs)
    
    # def get_permission_denied_message(self) -> str:
    #     return super().get_permission_denied_message()