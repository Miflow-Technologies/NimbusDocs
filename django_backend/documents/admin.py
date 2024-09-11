from django.contrib import admin
from .models import Document, Role, Folder, AccessControl, AuditLog

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'version', 'created_at', 'updated_at', 'owner', 'folder')
    search_fields = ('title', 'owner__username', 'folder__name')
    list_filter = ('created_at', 'updated_at', 'owner', 'folder')

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Folder)
class FolderAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent_folder', 'created_at', 'updated_at')
    search_fields = ('name', 'parent_folder__name')
    list_filter = ('created_at', 'updated_at')

@admin.register(AccessControl)
class AccessControlAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'document', 'folder', 'access_type')
    search_fields = ('user__username', 'role__name', 'document__title', 'folder__name')
    list_filter = ('access_type',)

@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'document', 'action', 'timestamp')
    search_fields = ('user__username', 'document__title', 'action')
    list_filter = ('action', 'timestamp')
