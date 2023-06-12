from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from account.models import CustomerUser


class CustomerMore(models.Model):
    user = models.OneToOneField(CustomerUser, related_name='C_user', on_delete=models.CASCADE)
    address = models.TextField(_('address'), max_length=250)
    Postal_code = models.IntegerField(_('Postal code'), blank=True)
    objects = models.Manager()

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = _('CustomerMore')
        verbose_name_plural = _('CustomersMore')


class Consignment(models.Model):
    class PackageType(models.TextChoices):
        PALLET = 'PALLET', 'Pallet'
        BOX = 'BOX', 'Box'
        BULK = 'BULK', 'Bulk'
        CONTAINER = 'CONTAINER', 'Container'

    name = models.CharField(_('name'), max_length=50)
    weight = models.IntegerField(_('weight'), blank=True)
    package_type = models.CharField(_('package type'), max_length=15, choices=PackageType.choices)
    number = models.CharField(_('number'), max_length=20, blank=True)
    origin_of_sending = models.CharField(_('origin of sending'), max_length=50)
    recipient_destination = models.CharField(_('recipient destination'), max_length=50)
    sender = models.ForeignKey(CustomerUser, related_name='consignment', on_delete=models.SET_NULL, null=True)
    recipient_name = models.CharField(_('recipient name'), max_length=50)
    recipient_number = PhoneNumberField(_('recipient phone number'), blank=False)

    objects = models.Manager()

    def __str__(self):
        return f'{self.sender} =>> {self.recipient_name}'

    class Meta:
        verbose_name = _('Consignment')
        verbose_name_plural = _('Consignments')
