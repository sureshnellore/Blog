from django.contrib import admin
from blog.models import Post
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'body', 'created', 'updated', 'publish', 'status']
    list_filter = ['publish', 'created']
    search_fields = ['status']
    raw_id_fields = ('author',)
    date_hierarchy = 'created'
    ordering = ['slug', 'created']

    prepopulated_fields = {'slug': ('title', )}


admin.site.register(Post, PostAdmin)

