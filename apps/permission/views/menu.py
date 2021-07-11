import json

from django.forms import model_to_dict
from rest_framework.decorators import action

from base.views import BaseModelViewSet
from base.response import json_ok_response, json_error_response
from ..models import Menu
from ..serializers import MenuSerializer


class MenuViewSet(BaseModelViewSet):
    queryset = Menu.objects.filter().order_by('-id')
    serializer_class = MenuSerializer
    ordering_fields = ('id', 'order')
    filter_fields = (
        'id',
        'pid'
    )
    search_fields = ('name', 'pid')

    @action(methods=['GET'], detail=False, )
    def parent(self, request, *args, **kwargs):
        parent_queryset = self.get_queryset().filter(pid=None).order_by('order')
        serializer = self.get_serializer(parent_queryset, many=True)

        return json_ok_response(serializer.data)

    @action(methods=['GET'], detail=False, )
    def tree(self, request, *args, **kwargs):
        t_l = []
        parent_queryset = self.get_queryset().filter(pid=None)
        for p_queryset in parent_queryset:
            menu = self.__format_res(self.get_serializer(p_queryset, many=False).data, many=False)
            children_queryset = self.get_queryset().filter(pid=p_queryset)
            menu['children'] = self.__format_res(self.get_serializer(children_queryset, many=True).data, many=True)
            t_l.append(menu)
        print(t_l)

        return json_ok_response(t_l)

    def __format_res(self, data, many):
        if not many:
            res_dic = {
                'path': data['path'],
                'component': data['component'],
                'name': data['name'],
                'redirect': data['redirect'],
                'hidden': data['hidden'],
                'alwaysShow': data['always_show'],
                'meta': {
                    'title': data['title'],
                    'roles': data['roles'],
                    'icon': data['icon'],
                    'noCache': data['no_cache'],
                    'breadcrumb': data['breadcrumb'],
                    'affix': data['affix'],
                }
            }
            return res_dic
        else:
            res_list = []
            for item in json.loads(json.dumps(data)):
                res_dic = {
                    'path': item['path'],
                    'component': item['component'],
                    'name': item['name'],
                    'redirect': item['redirect'],
                    'hidden': item['hidden'],
                    'meta': {
                        'title': item['title'],
                        'roles': item['roles'],
                        'icon': item['icon'],
                        'noCache': item['no_cache'],
                        'breadcrumb': item['breadcrumb'],
                        'affix': item['affix'],
                        'activeMenu': item['active_menu'],
                    }
                }
                if item['active_menu']:
                    res_dic['meta'] = item['active_menu']
                res_list.append(res_dic)
            return res_list
