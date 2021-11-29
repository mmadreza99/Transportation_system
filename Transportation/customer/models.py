from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
from phonenumber_field.modelfields import PhoneNumberField

User = get_user_model()


class CustomerMore(models.Model):
    user = models.OneToOneField(User, related_name='C_user', on_delete=models.CASCADE)
    address = models.TextField(_('address'), max_length=250)
    Postal_code = models.IntegerField(_('Postal code'), blank=True)

    def __str__(self):
        return self.user


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
    sender = models.ForeignKey(CustomerMore, related_name='consignment', on_delete=models.SET_NULL)
    recipient_name = models.CharField(_('recipient name'), max_length=50)
    recipient_number = PhoneNumberField(_('phone_number'), blank=False)

    class Meta:
        verbose_name = _('CustomerUser')
        verbose_name_plural = _('CustomersUser')
