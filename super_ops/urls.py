"""super_ops URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers

urlpatterns = [
    path('admin/', admin.site.urls),
]

from apps.permission.router import router as prem_router
from apps.user.router import router as user_router
from apps.cmdb.router import router as cmdb_router

router = routers.DefaultRouter()
router.registry.extend(prem_router.registry)
router.registry.extend(user_router.registry)
router.registry.extend(cmdb_router.registry)

urlpatterns += [
    path('api/', include(router.urls)),
]

# JWT
from base.rest_framework_jwt import obtain_jwt_token
from base.rest_framework_jwt import refresh_jwt_token
from base.rest_framework_jwt import verify_jwt_token
from apps.permission import urls as rbac_url
from apps.user import urls as user_url
from django.conf import settings
from django.views.static import serve

# JWT
urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    path('api/v1/user/login/', obtain_jwt_token),
    path('api/v1/token-refresh/', refresh_jwt_token),
    path('api/v1/token-verify/', verify_jwt_token),
    path('api/', include(rbac_url)),
    path('api/', include(user_url)),

]
