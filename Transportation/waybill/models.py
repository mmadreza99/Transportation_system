from django.db import models
from django.utils.translation import gettext_lazy as _

from account.models import DriverUser
from customer.models import CustomerUser, Consignment


class Waybill(models.Model):
    driver = models.ForeignKey(DriverUser, on_delete=models.SET_NULL, related_name='waybill_driver', null=True)
    sender = models.ForeignKey(CustomerUser, on_delete=models.SET_NULL, related_name='waybill_sender', null=True)
    consignment = models.ForeignKey(
        Consignment, on_delete=models.SET_NULL, related_name='waybill_consignment', null=True
    )
    created_on = models.DateTimeField(_('create on'), auto_now_add=True)
    more = models.JSONField(_('more'), null=True, blank=True)

    def __str__(self):
        return f'''consignment: {self.consignment.__str__()}| \
                driver :{self.driver.__str__()}| \
                sender: {self.sender.__str__()}'''
