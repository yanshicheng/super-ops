from .response import json_ok_response, json_error_response

from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView


class BaseModelViewSet(ModelViewSet):
    """
        视图集合基类
    """

    def create(self, request, *args, **kwargs):
        response = super(BaseModelViewSet, self).create(request, *args, **kwargs)
        return json_ok_response(response.data)

    def update(self, request, *args, **kwargs):
        response = super(BaseModelViewSet, self).update(request, *args, **kwargs)
        return json_ok_response(response.data)

    def destroy(self, request, *args, **kwargs):
        response = super(BaseModelViewSet, self).destroy(request, *args, **kwargs)
        return json_ok_response(response.data)

    def list(self, request, *args, **kwargs):
        try:
            ordering = request.query_params.get('ordering', '')
            ordering = ordering.replace('+', '').strip()
            if ordering:
                if self.serializer_class is None:
                    queryset = self.filter_queryset(self.get_serializer_class().Meta.model.objects.order_by(ordering))
                else:
                    queryset = self.filter_queryset(self.serializer_class.Meta.model.objects.order_by(ordering))
            else:
                queryset = self.filter_queryset(self.get_queryset())
            page = request.query_params.get('page', '')
            size = request.query_params.get('size', '')
            if page or size:
                page_queryset = self.paginate_queryset(queryset)
                if page is not None:
                    serializer = self.get_serializer(page_queryset, many=True)
                    return self.get_paginated_response(serializer.data)
            serializer = self.get_serializer(queryset, many=True)
            return json_ok_response(data=serializer.data)
        except Exception as e:
            return json_error_response(message=str(e))


    def retrieve(self, request, *args, **kwargs):
        response = super(BaseModelViewSet, self).retrieve(request, *args, **kwargs)
        return json_ok_response(response.data)


class BaseApiView(APIView):
    """
        APIView视图类
    """
    pass
    # authentication_classes = [JSONWebTokenAuthentication]
    # permission_classes = [IsAuthenticated, ]

# class TreeModelViewSet(BaseModelViewSet):
#     serializer_class = TreeSerializer
#
#     def list(self, request, *args, **kwargs):
#         queryset = self.filter_queryset(self.get_queryset())
#         page = self.paginate_queryset(queryset)
#         s = self.get_serializer(queryset, many=True)
#         response = []
#         try:
#             tree_dict = {item['id']: item for item in s.data}
#             for i in tree_dict:
#                 if tree_dict[i]['pid']:
#                     pid = tree_dict[i]['pid']
#                     parent = tree_dict[pid]
#                     parent.setdefault('children', []).append(tree_dict[i])
#                 else:
#                     response.append(tree_dict[i])
#         except KeyError:
#             response = s.data
#         if page is not None:
#             response = self.get_paginated_response(response)
#             return json_ok_response(response.data)
#         return json_ok_response(response)
