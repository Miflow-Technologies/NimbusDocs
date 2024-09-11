from rest_framework import serializers
from .models import Document, Role, Folder, AccessControl, AuditLog
from django.contrib.auth.models import User

# Serializer for User (if needed for API endpoints)
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

# Serializer for Document
class DocumentSerializer(serializers.ModelSerializer):
    owner = UserSerializer()  # Nested serializer for user details
    folder = serializers.StringRelatedField()  # Display folder name

    class Meta:
        model = Document
        fields = ['id', 'title', 'file', 'version', 'created_at', 'updated_at', 'owner', 'folder']

# Serializer for Role
class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'name']

# Serializer for Folder
class FolderSerializer(serializers.ModelSerializer):
    parent_folder = serializers.StringRelatedField()  # Display parent folder name

    class Meta:
        model = Folder
        fields = ['id', 'name', 'parent_folder', 'created_at', 'updated_at']

# Serializer for AccessControl
class AccessControlSerializer(serializers.ModelSerializer):
    user = UserSerializer()  # Nested serializer for user details
    role = RoleSerializer()  # Nested serializer for role details
    document = DocumentSerializer()  # Nested serializer for document details
    folder = FolderSerializer()  # Nested serializer for folder details

    class Meta:
        model = AccessControl
        fields = ['id', 'user', 'role', 'document', 'folder', 'access_type']

# Serializer for AuditLog
class AuditLogSerializer(serializers.ModelSerializer):
    user = UserSerializer()  # Nested serializer for user details
    document = DocumentSerializer()  # Nested serializer for document details

    class Meta:
        model = AuditLog
        fields = ['id', 'user', 'document', 'action', 'timestamp']
