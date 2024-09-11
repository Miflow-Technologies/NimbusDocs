from rest_framework import viewsets
from .models import Document, Role, Folder, AccessControl, AuditLog
from .serializers import DocumentSerializer, RoleSerializer, FolderSerializer, AccessControlSerializer, AuditLogSerializer

# ViewSet for Document
class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

# ViewSet for Role
class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

# ViewSet for Folder
class FolderViewSet(viewsets.ModelViewSet):
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer

# ViewSet for AccessControl
class AccessControlViewSet(viewsets.ModelViewSet):
    queryset = AccessControl.objects.all()
    serializer_class = AccessControlSerializer

# ViewSet for AuditLog
class AuditLogViewSet(viewsets.ModelViewSet):
    queryset = AuditLog.objects.all()
    serializer_class = AuditLogSerializer
