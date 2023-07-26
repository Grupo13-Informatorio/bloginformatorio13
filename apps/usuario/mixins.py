from django.contrib.auth.mixins import PermissionRequiredMixin

class IsMiembroRequiredMixin(PermissionRequiredMixin):

    permission_required = ["is_miebro", "is_superuser"]
   