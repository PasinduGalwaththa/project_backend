from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Customuser

class CustomuserAdmin(UserAdmin):
    # Fields to be displayed and made editable in the main list view
    list_display = ('username', 'email', 'usertype')

    # Fields to be displayed in the detail view and marked as read-only
    readonly_fields = ('id', 'date_joined', 'last_login')

    # Fieldsets to separate the fields in the edit view
    fieldsets = (
        (None, {
            'fields': ('username', 'password', 'email', 'usertype')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name'),
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined'),
        }),
    )

    # Override to exclude all other User fields from the form in add view
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'email', 'usertype'),
        }),
    )

# Register the Customuser model with the custom admin class
admin.site.register(Customuser, CustomuserAdmin)
