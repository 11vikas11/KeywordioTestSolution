from django.contrib import admin
from .models import AdminUser, Book

admin.site.register(AdminUser)
admin.site.register(Book)

