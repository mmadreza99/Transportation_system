from django.db import models
from django.utils.translation import gettext_lazy as _

from drivers.models import DriverMore
from customer.models import CustomerUser, Consignment, CustomerMore

import random
import string


class Waybill(models.Model):
    driver = models.ForeignKey(DriverMore, on_delete=models.SET_NULL, related_name='waybill_driver', null=True)
    sender = models.ForeignKey(CustomerMore, on_delete=models.SET_NULL, related_name='waybill_sender', null=True)
    consignment = models.ForeignKey(
        Consignment, on_delete=models.SET_NULL, related_name='waybill_consignment', null=True
    )
    created_on = models.DateTimeField(_('create on'), auto_now_add=True, auto_created=True)
    more = models.JSONField(_('more'), null=True, blank=True)
    track_code = models.CharField(_('track_code'), max_length=20, unique=True, null=True, blank=True)

    def __str__(self):
        return f'''consignment: {self.consignment}| \
                driver :{self.driver}| \
                sender: {self.sender}'''

    @staticmethod
    def generate_track_code():
        # Define the set of characters to use in the track code
        chars = string.ascii_uppercase + string.digits

        # Generate a random track code of the desired length
        track_code = ''.join(random.choices(chars, k=20))

        obj_track_code = Waybill.objects.filter(track_code=track_code).first()
        if obj_track_code:
            track_code = Waybill.generate_track_code()
            return track_code
        return track_code
