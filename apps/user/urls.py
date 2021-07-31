from .views.user_profile import UserInfoApiView, UserLogoutApiView
from django.urls import path, include

urlpatterns = [
    path('v1/user/info/', UserInfoApiView.as_view()),
    path('v1/user/logout/', UserLogoutApiView.as_view()),
]