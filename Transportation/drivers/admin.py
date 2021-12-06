from django.contrib import admin
from .models import Truck, DriverMore, Certificate, KartHoshmand


class TruckAdmin(admin.ModelAdmin):
    list_display = ('type', 'id_insurance', 'registration_plate')
    list_filter = ('type',)


class DriverAdmin(admin.ModelAdmin):
    list_display = ('user', 'truck', 'Driver_licence')

    fieldsets = (
        ('Personal info', {
            'fields': (
                'user',
                'Date_of_birth',
                'place_of_birth',
                'truck',
                'Driver_licence',
                'kart_hoshmand',
                'address'
            )
        }),
    )


class CertificateAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'created_time')
    list_filter = ('type',)


class KartHoshmandAdmin(admin.ModelAdmin):
    list_display = ('id', 'validity_date', 'create_time')


admin.site.register(Truck, TruckAdmin)
admin.site.register(DriverMore, DriverAdmin)
admin.site.register(Certificate, CertificateAdmin)
admin.site.register(KartHoshmand, KartHoshmandAdmin)
