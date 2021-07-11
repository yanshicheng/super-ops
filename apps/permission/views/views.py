from django.shortcuts import render

# Create your views here.
from base.views import BaseApiView
from base.response import json_error_response, json_ok_response


class LoginViewSet(BaseApiView):
    def post(self, request):
        import casbin
        # from casbin_adapter.adapter import Adapter
        #
        # adapter = Adapter()
        # e = casbin.Enforcer('./model.conf', adapter, True)
        #
        # sub = "alice"  # the user that wants to access a resource.
        # obj = "data1"  # the resource that is going to be accessed.
        # act = "read"  # the operation that the user performs on the resource.
        #
        # if e.enforce(sub, obj, act):
        #     # permit alice to read data1casbin_django_orm_adapter
        #     print('ok')
        # else:
        #     # deny the request, show an error
        #     print('rttot')
        # import casbin
        # from casbin_adapter.adapter import Adapter
        # from ..adapter import Adapter as ad
        # # adapter = Adapter()
        # ad = ad()
        # import os
        # print()
        # x = casbin.Enforcer(os.path.join(os.getcwd(), 'rbac', 'model.conf'),
        #                     ad)
        # sub = "admin"  # the user that wants to access a resource.
        # obj = "/api/212"  # the resource that is going to be accessed.
        # act = "GET"  # the operation that the user performs on the resource.
        # if x.enforce(sub, obj, act):
        #     print('ok')
        # print(x.get_policy())
        # print(x.get_permissions_for_user('zhang'))
        # # sub = "zhang"  # 想要访问资源的用户
        # obj = "data"  # 将要被访问的资源
        # act = "read"  # 用户对资源进行的操作
        # e.add_policy(sub, obj, act)
        #
        # e.save_policy()
        # if e.enforce(sub, obj, act):
        #     # permit alice to read data1casbin_django_orm_adapter
        #     print('ok')
        # else:
        #     # deny the request, show an error
        #     print('rttot')
        # # roles = e.get_roles_for_user("zhang")
        return json_error_response(message='email和password为必传参数!', )
