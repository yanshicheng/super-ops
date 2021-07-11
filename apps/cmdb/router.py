from rest_framework import routers
from .views.classify import ClassifyViewSet
from .views.field import FieldsViewSet
from .views.asset import AssetViewSet
from .views.record import ChangeRecordViewSet

# from .views.table_relation import SchemaRelationViewSet

router = routers.DefaultRouter()
router.register(r'v1/cmdb/classify', ClassifyViewSet)
router.register(r'v1/cmdb/field', FieldsViewSet)
router.register(r'v1/cmdb/asset', AssetViewSet)
router.register(r'v1/cmdb/record', ChangeRecordViewSet)
