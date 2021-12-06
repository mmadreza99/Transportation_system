from django.contrib import admin

# Register your models here.
from .models import AuthorMore, Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ("status",)
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'content']


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('user', 'nickname')
    search_fields = ['user', 'nickname']


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'body', 'active', 'created_on')
    list_filter = ("active",)
    search_fields = ['active', 'create_on']


admin.site.register(Post, PostAdmin)
admin.site.register(AuthorMore, AuthorAdmin)
admin.site.register(Comment, CommentAdmin)
