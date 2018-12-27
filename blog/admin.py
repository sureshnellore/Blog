from django.contrib import admin
from blog.models import Post
from blog.models import Comment
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'body', 'created', 'updated', 'publish', 'status']
    list_filter = ['publish', 'created']
    search_fields = ['status']
    raw_id_fields = ('author',)
    date_hierarchy = 'created'
    ordering = ['slug', 'created']

    prepopulated_fields = {'slug': ('title', )}


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'body', 'created', 'updated', 'active')
    list_filter = ['created', 'updated', 'active']
    search_fields = ['name', 'email', 'body']


admin.site.register(Comment, CommentAdmin)
admin.site.register(Post, PostAdmin)

