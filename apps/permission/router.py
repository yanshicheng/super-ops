from rest_framework import routers
from .views.role import RoleViewSet
from .views.rule import RoleRuleViewSet
from .views.menu import MenuViewSet

# from .views.table_relation import SchemaRelationViewSet

router = routers.DefaultRouter()
router.register(r'v1/prem/role', RoleViewSet)
router.register(r'v1/prem/rule', RoleRuleViewSet)
router.register(r'v1/prem/menu', MenuViewSet)
# router.register(r'v1/prem/rule-classify', RuleClassifyViewSet)
