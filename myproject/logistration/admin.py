from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .models import UserProfile

User = get_user_model()  # Get the Django User model dynamically


class UserProfileInline(admin.StackedInline):
    model = UserProfile  # Inline model for UserProfile


class CustomUserAdmin(UserAdmin):
    inlines = (UserProfileInline,)  # Add UserProfileInline to the UserAdmin


admin.site.unregister(User)  # Unregister the default UserAdmin
admin.site.register(User, CustomUserAdmin)  # Register the CustomUserAdmin with the User model
