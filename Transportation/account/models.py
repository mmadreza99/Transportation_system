from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    class Types(models.TextChoices):
        DRIVER = 'DRIVER', 'Driver'
        CUSTOMER = 'CUSTOMER', 'Customer'
        AUTHOR = 'AUTHOR', 'Author'

    type = models.CharField(_('Type'), max_length=50, choices=Types.choices, default=Types.DRIVER)
    phone_number = models.CharField(_('phone_number'), max_length=11, blank=True)
    Social_Security = models.CharField(_('Social_Security'), max_length=10, blank=True)
    avatar = models.ImageField(upload_to='avatar', blank=True)
    is_active = models.BooleanField(
        _('active'),
        default=False,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )


class DriverManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.DRIVER)


class DriverUser(User):
    objects = DriverManager()
    base_type = User.Types.DRIVER

    class Meta:
        proxy = True


class CustomerManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.CUSTOMER)


class CustomerUser(User):
    objects = CustomerManager()
    base_type = User.Types.CUSTOMER

    class Meta:
        proxy = True


class AuthorManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.AUTHOR)


class AuthorUser(User):
    base_type = User.Types.AUTHOR
    objects = AuthorManager()

    class Meta:
        proxy = True
