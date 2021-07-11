from base.views import BaseModelViewSet
from base.response import json_ok_response, json_error_response
from ..models import RuleClassify, Rule
from ..serializers import RuleClassifySerializer, RuleSerializer
from rest_framework.decorators import action


class RuleClassifyViewSet(BaseModelViewSet):
    queryset = RuleClassify.objects.filter().order_by('-id')
    serializer_class = RuleClassifySerializer
    ordering_fields = ('id',)
    filter_fields = (
        'id',
        'name',
    )
    search_fields = ('name',)

    @action(methods=['GET'], detail=False, )
    def tree(self, request, *args, **kwargs):
        t_l = []
        all_queryset = self.get_queryset()
        for inc in all_queryset:
            parent_ser = self.get_serializer(inc, many=False)
            children_inc = Rule.objects.filter(rule_classify=inc)
            parent_dic = parent_ser.data
            parent_dic['children'] = RuleSerializer(children_inc, many=True).data
            t_l.append(parent_dic)
        return json_ok_response(t_l)
