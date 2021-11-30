from django.contrib import admin

# Register your models here.
from .models import Author, Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ("status",)
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'content']


class AuthorAdmin(admin.ModelAdmin):
    def username(self):
        return self.__str__()

    list_display = (username, 'nickname')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'body', 'active', 'created_on')
    list_filter = ("user",)
    search_fields = ['active', 'create_on']


admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Comment)
