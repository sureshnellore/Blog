from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


# Create your models here.

'''class CustomManager(models.manager):
    def get_queryset(self):
        return super().get_queryset.filter(status='published')'''


class Post(models.Model):

    STATIC_CHOICE = (('draft', 'Draft'), ('published', 'Published'))
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=264, unique_for_date='publish')
    author = models.ForeignKey(User, related_name='blog_posts', on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    publish = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices=STATIC_CHOICE, default='draft')
    #objects = CustomManager()

    class Meta:
        ordering = ('-publish', )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_details', args=[self.publish.year, self.publish.strftime('%m'), self.publish.strftime('%d'),self.slug])







