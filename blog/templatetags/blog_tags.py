from django import template 
from blog.models import Post 
from django.db.models import Count
register=template.Library() 

@register.simple_tag 
def total_posts(): 
    return Post.objects.count() 

@register.inclusion_tag('blog/latest_posts123.html') 
def show_latest_posts(count=5): 
    latest_posts=Post.objects.order_by('-publish')[:count] 
    return {'latest_posts':latest_posts} 

