from django.contrib import admin
from .models import DriverUser, CustomerUser, AuthorUser


class UserAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {
            'fields': (
                'first_name',
                'last_name',
                'email',
                'Social_Security',
                'phone_number',
                'avatar'
            )
        }),
        ('Permissions', {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
                'is_available',
                'groups',
                'user_permissions'
            ),
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'phone_number',
        'is_staff',
    )

    search_fields = (
        'username',
        'first_name',
        'last_name',
        'phone_number',
        'email',
    )


admin.site.register(DriverUser, UserAdmin)
admin.site.register(CustomerUser, UserAdmin)
admin.site.register(AuthorUser, UserAdmin)
