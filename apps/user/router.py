from rest_framework import routers
from .views.user_profile import UserProfileViewSet
from .views.department import DepartmentViewSet

# from .views.table_relation import SchemaRelationViewSet

router = routers.DefaultRouter()
router.register(r'v1/user/user-profile', UserProfileViewSet)
router.register(r'v1/user/department', DepartmentViewSet)
