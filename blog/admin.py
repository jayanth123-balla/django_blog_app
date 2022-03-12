from django.contrib import admin
from blog.models import Post,Comment

class PostAdmin(admin.ModelAdmin):
    list_display=['title','slug','author','publish','created','updated','status','body']
    list_filter=('status','created','publish','author')
    search_fields=('title','body')
    prepopulated_fields={'slug':('title',)}
    raw_id_fields=('author',)
    ordering=['status','publish']


class CommentAdmin(admin.ModelAdmin): 
    list_display=('name','email','post','body','created','updated','active') 
    list_filter=('active','created','updated') 
    search_fields=('name','email','body') 

admin.site.register(Post,PostAdmin) 
admin.site.register(Comment,CommentAdmin) 
