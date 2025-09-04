from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, UserProfile

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = "user_profile"


class CustomUserAdmin(BaseUserAdmin):
    inlines = [UserProfileInline]

    list_display = ['username', 'display_name', 'first_name', 'last_name', 'email', 'is_active', 'is_superuser', 'is_staff']

    def display_name(self, obj):
        return obj.userprofile.display_name

admin.site.register(User, CustomUserAdmin)
