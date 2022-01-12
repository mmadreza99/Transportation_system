from django.contrib import admin
from .models import Truck, DriverMore, Certificate, KartHoshmand


class TruckInLine(admin.StackedInline):
    model = Truck


class CertificateInLine(admin.StackedInline):
    model = Certificate


class KartHoshmandInLine(admin.StackedInline):
    model = KartHoshmand


@admin.register(DriverMore)
class DriverAdmin(admin.ModelAdmin):
    list_display = ('user',)

    fieldsets = (
        ('Personal info', {
            'fields': (
                'user',
                'Date_of_birth',
                'place_of_birth',
                'address'
            )
        }),
    )

    inlines = [TruckInLine, CertificateInLine, KartHoshmandInLine]




