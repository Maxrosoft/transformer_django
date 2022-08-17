from django import template
from ..models import Post
from django.db.models import Count

register = template.Library()


@register.simple_tag
def total_posts():
    return Post.published.count()


@register.inclusion_tag('main/posts/post/latest_posts.html')
def get_latest_posts(count=5):
    latest_posts = Post.published.all()[:count]
    return {'latest_posts': latest_posts}


@register.inclusion_tag('main/posts/post/most_commented_posts.html')
def get_most_commented_posts(count=5):
    most_commented_posts = Post.published.annotate(
        total_comments=Count('comments')).order_by('-total_comments')[:count]
    return {'most_commented_posts': most_commented_posts}
