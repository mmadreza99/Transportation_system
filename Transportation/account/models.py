from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    class Types(models.TextChoices):
        DRIVER = 'DRIVER', 'Driver'
        CUSTOMER = 'CUSTOMER', 'Customer'
        AUTHOR = 'AUTHOR', 'Author'

    base_type = Types.DRIVER
    type = models.CharField(_('Type'), max_length=50, choices=Types.choices, default=base_type)
    phone_number = PhoneNumberField(_('phone_number'), blank=False, unique=True)
    Social_Security = models.CharField(_('Social_Security'), max_length=10, blank=True)
    avatar = models.ImageField(upload_to='avatar', blank=True)
    is_available = models.BooleanField(
        _('available'),
        default=False,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )


class DriverManager(UserManager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.DRIVER)


class DriverUser(User):
    objects = DriverManager()
    base_type = User.Types.DRIVER

    @property
    def more(self):
        return self.D_user

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Types.DRIVER
        return super().save(*args, **kwargs)

    class Meta:
        proxy = True


class CustomerManager(UserManager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.CUSTOMER)


class CustomerUser(User):
    objects = CustomerManager()
    base_type = User.Types.CUSTOMER

    @property
    def more(self):
        return self.C_user

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Types.CUSTOMER
        return super().save(*args, **kwargs)

    class Meta:
        proxy = True


class AuthorManager(UserManager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.AUTHOR)


class AuthorUser(User):
    base_type = User.Types.AUTHOR
    objects = AuthorManager()

    @property
    def more(self):
        return self.A_user

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Types.AUTHOR
        return super().save(*args, **kwargs)

    class Meta:
        proxy = True
