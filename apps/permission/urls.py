from .views.views import LoginViewSet
from django.urls import path, include


urlpatterns = [
    path('v1/user/', LoginViewSet.as_view()),
]
