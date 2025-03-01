from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import UserProfile

admin.site.register(UserProfile)
from django.contrib.auth.models import User, Permission

perm_add = Permission.objects.get(codename="can_add_book")
perm_edit = Permission.objects.get(codename="can_change_book")
perm_delete = Permission.objects.get(codename="can_delete_book")

user.user_permissions.add(perm_add, perm_edit, perm_delete)
user.save()
