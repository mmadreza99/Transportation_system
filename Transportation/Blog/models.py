from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from account.models import AuthorUser


class AuthorMore(models.Model):
    user = models.OneToOneField(AuthorUser, related_name='A_user', on_delete=models.CASCADE)
    nickname = models.CharField(_('nickname'), max_length=50, blank=True)

    def __str__(self):
        return f'{self.user}'

    class Meta:
        verbose_name = _('AuthorMore')
        verbose_name_plural = _('AuthorsMores')


class Post(models.Model):
    objects = models.Manager()

    class Status(models.IntegerChoices):
        DRAFT = 0, "Draft"
        PUBLISH = 1, "Publish"

    title = models.CharField(_('title'), max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(_('description'))
    author = models.ForeignKey(AuthorUser, related_name='post', on_delete=models.SET_NULL, null=True)
    attachment = models.ImageField(_('attachment'), upload_to='attachment')
    status = models.SmallIntegerField(choices=Status.choices, default=0)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'post {} by {}'.format(self.title, self.author)

    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')
        ordering = ['-created_on']


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(get_user_model(), related_name='comment', on_delete=models.CASCADE, null=True, blank=True)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.user)
