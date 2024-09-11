from django.db import models
from django.contrib.auth.models import User

# Role Model
class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

# Folder Model
class Folder(models.Model):
    name = models.CharField(max_length=255)
    parent_folder = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# Document Model
class Document(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='documents/')
    version = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    folder = models.ForeignKey(Folder, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title

# AccessControl Model
class AccessControl(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    document = models.ForeignKey(Document, null=True, blank=True, on_delete=models.SET_NULL)
    folder = models.ForeignKey(Folder, null=True, blank=True, on_delete=models.SET_NULL)
    access_type = models.CharField(max_length=50)  # e.g., read, write, delete

    def __str__(self):
        return f"{self.user.username} - {self.access_type}"

# AuditLog Model
class AuditLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    action = models.CharField(max_length=50)  # e.g., created, updated, deleted
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.action} - {self.timestamp}"
