from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class BaseUser(AbstractUser):
    phone_number = models.CharField(_('phone_number'), max_length=11, blank=True)
    Social_Security = models.CharField(_('Social_Security'), max_length=10, blank=True)
    avatar = models.ImageField(upload_to='media/avatar/', blank=True)

    class Meta:
        verbose_name = _('BaseUser')
        verbose_name_plural = _('BaseUsers')

