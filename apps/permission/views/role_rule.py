from base.views import BaseModelViewSet
from base.response import json_ok_response, json_error_response
from ..models import Rule
from ..serializers import RuleSerializer


class RoleRuleViewSet(BaseModelViewSet):
    queryset = Rule.objects.filter().order_by('-id')
    serializer_class = RuleSerializer
    ordering_fields = ('id',)
    filter_fields = (
        'id',
        'name',
        'rule_classify_id'
    )
    search_fields = ('name',)
