from rest_framework import routers
from .views import views
from .views import node_link_clyssify
from .views import node_link_asset

router = routers.DefaultRouter()
router.register('v1/service-tree/nodes', views.ServiceTreeModelViewSet, basename='service_tree_node')
router.register('v1/service-tree/opera-permission', views.NodeOperaPermissionModelViewSet,
                basename='link_opera_permission')
# router.register('v1/service-tree/server', views.NodeLinkServerModelViewSet, basename='link_server')
router.register('v1/service-tree/tag', views.NodeLinkTagModelViewSet, basename='link_tag')
router.register('v1/service-tree/node-link-classify', node_link_clyssify.NodeLinkClassifyViewSet,
                basename='link_classify')
router.register('v1/service-tree/node-link-asset', node_link_asset.NodeLinkAssetViewSet,
                basename='unlink_classify')
