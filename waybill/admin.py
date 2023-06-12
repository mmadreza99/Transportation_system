from django.contrib import admin
from .models import Waybill


class WaybillAdmin(admin.ModelAdmin):
    list_display = ('driver', 'sender', 'consignment')


admin.site.register(Waybill, WaybillAdmin)
