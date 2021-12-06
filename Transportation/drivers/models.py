from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model


class Certificate(models.Model):
    class Type(models.TextChoices):
        P1 = 'P1', 'p1'
        P2 = 'P2', 'p2'
        P3 = 'P3', 'p3'
    id = models.CharField(_('id'), max_length=20, primary_key=True)
    created_time = models.DateTimeField(_('create time'))
    validity_date = models.DateTimeField(_('validity date'))
    type = models.CharField(_('type'), max_length=10, choices=Type.choices)
    image = models.ImageField(_('image'), upload_to='Certificate', null=True)

    def __str__(self):
        return str(self.id)


class KartHoshmand(models.Model):
    id = models.CharField(_('id'), max_length=20, primary_key=True)
    validity_date = models.DateField(_('validity date'))
    create_time = models.DateField(_('create time'))
    image = models.ImageField(_('image'), upload_to='kart_hoshmand', null=True)

    def __str__(self):
        return str(self.id)


class Truck(models.Model):
    class Types(models.TextChoices):
        PICKUP = 'PICKUP', 'Pickup'
        BOX_TRUCK = 'BOX_TRUCK', 'Box_truck'
        FLATBED_TRUCK = 'FLATBED_TRUCK', 'flatbed_truck'
        DUMP_TRUCK = 'DUMP_TRUCK', 'Dump_truck'
        TANK_TRUCK = 'TANK_TRUCK', 'Tank_truck'
        CAR_TRANSPORT = 'CAR_TRANSPORT', 'Car_transport'
        HEAVY = 'HEAVY', 'Heavy'
    type = models.CharField(_('type'), max_length=15, choices=Types.choices)
    registration_plate = models.CharField(_('registration plate'), max_length=8)
    id_insurance = models.IntegerField(_('id insurance'))
    image = models.ImageField(_('image'), upload_to='truck')

    def __str__(self):
        return f'{self.type}, {self.registration_plate}'


class DriverMore(models.Model):
    user = models.OneToOneField(get_user_model(), related_name='D_user', on_delete=models.CASCADE)
    Date_of_birth = models.DateTimeField(_('birth'), null=True)
    place_of_birth = models.CharField(_('place of birth'), max_length=50, blank=True)
    Driver_licence = models.ForeignKey(Certificate, related_name='Driver', on_delete=models.CASCADE)
    address = models.TextField(_('address'), max_length=150, blank=True)
    kart_hoshmand = models.OneToOneField(KartHoshmand, on_delete=models.CASCADE)
    truck = models.OneToOneField(Truck, on_delete=models.CASCADE)
    # TODO ADD PHONE NUMBER

    def __str__(self):
        return f'{self.user} phone number: {self.user.phone_number}'

    class Meta:
        verbose_name = _('DriverUser')
        verbose_name_plural = _('DriversUser')
