from django.contrib import admin

from .models import CustomerMore, Consignment


class CustomerAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Personal info', {
            'fields': (
                'user',
                'address',
                'Postal_code'
            )
        }),
    )

    def phone_number(self):
        return self.user.phone_number

    def is_active(self):
        return self.user.is_active

    list_display = ('user', phone_number, is_active)


class ConsignmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'package_type', 'sender', 'recipient_name')
    search_fields = ['package_type', ]


admin.site.register(CustomerMore, CustomerAdmin)
admin.site.register(Consignment, ConsignmentAdmin)
