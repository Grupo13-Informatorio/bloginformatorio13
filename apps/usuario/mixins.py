from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required

class IsMiembroRequiredMixin(PermissionRequiredMixin):

    permission_required = ["is_miebro", "is_superuser"]
   