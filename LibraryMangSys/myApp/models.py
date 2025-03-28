from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
class AdminUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    groups = models.ManyToManyField(Group, related_name="admin_users")
    user_permissions = models.ManyToManyField(Permission, related_name="admin_users_permissions")

    class Meta:
        db_table = "admin_user"

class Book(models.Model):
    title= models.CharField(max_length=200)
    author= models.CharField(max_length=200)
    isbn = models.CharField(max_length=13, unique=True)
    publishedDate= models.DateField()
    available= models.BooleanField(default=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        db_table = "book"
