from blog.models import Post
from django import template
register = template.Library()
from django.db.models import Count

@register.simple_tag
def total_posts():
    return Post.objects.count()


@register.inclusion_tag('blog/latestposts.html')
def show_latest_posts():
    late_posts = Post.objects.order_by('-publish')[:4]
    return {'late_posts': late_posts}


@register.simple_tag
def get_most_commented_posts():
    return Post.objects.annotate(total_comments=Count('comments')).order_by('-total_comments')[:Count]


