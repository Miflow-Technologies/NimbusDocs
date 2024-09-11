from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DocumentViewSet, RoleViewSet, FolderViewSet, AccessControlViewSet, AuditLogViewSet

router = DefaultRouter()
router.register(r'documents', DocumentViewSet)
router.register(r'roles', RoleViewSet)
router.register(r'folders', FolderViewSet)
router.register(r'access-controls', AccessControlViewSet)
router.register(r'audit-logs', AuditLogViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
