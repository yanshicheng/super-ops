from rest_framework.decorators import action

from base.views import BaseModelViewSet
from base.response import json_ok_response, json_error_response
from ..models import Role
from ..serializers import RoleSerializer


class RoleViewSet(BaseModelViewSet):
    queryset = Role.objects.filter().order_by('-id')
    serializer_class = RoleSerializer
    ordering_fields = ('id',)
    filter_fields = (
        'id',
    )
    search_fields = ('name',)


