from django.contrib import admin
from .models import Article,Category,Tag
from django_comments.models import Comment

# Register your models here.

class ArticlePostAdmin(admin.ModelAdmin):
	list_display = ('title','date','category')

# class CommentPostAdmin(admin.ModelAdmin):
# 	list_display = ('article','nickname','email','date')

admin.site.register(Article,ArticlePostAdmin)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Tag)
