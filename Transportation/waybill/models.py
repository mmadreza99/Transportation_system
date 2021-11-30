from django.db import models
from django.utils.translation import gettext_lazy as _
from drivers.models import DriverMore
from customer.models import CustomerMore, Consignment


class Waybill(models.Model):
    driver = models.ForeignKey(DriverMore, on_delete=models.SET_NULL, related_name='waybill', null=True)
    sender = models.ForeignKey(CustomerMore, on_delete=models.SET_NULL, related_name='waybill', null=True)
    consignment = models.ForeignKey(Consignment, on_delete=models.SET_NULL, related_name='waybill', null=True)
    created_on = models.DateTimeField(_('create on'), auto_now_add=True)
    more = models.JSONField(_('more'))

    def __str__(self):
        return f'consignment: {self.consignment.__str__()}' \
               f',driver :{self.driver.__str__()},' \
               f' sender: {self.sender.__str__()}'
