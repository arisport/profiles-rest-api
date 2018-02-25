from django.contrib import admin

from . import models


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'is_staff', 'is_gay')

# Register your models here.
admin.site.register(models.UserProfile, UserAdmin)