from base.views import BaseModelViewSet
from base.response import json_ok_response, json_error_response
from ..models import Department
from ..serializers import DepartmentSerializer


class DepartmentViewSet(BaseModelViewSet):
    queryset = Department.objects.filter().order_by('-id')
    serializer_class = DepartmentSerializer
    ordering_fields = ('id',)
    filter_fields = (
        'id',
    )
    search_fields = ('name',)