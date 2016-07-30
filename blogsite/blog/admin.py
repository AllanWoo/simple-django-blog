from django.contrib import admin
from .models import Article,Comment,Category,Tag
# Register your models here.

class ArticlePostAdmin(admin.ModelAdmin):
	list_display = ('title','date','category')

class CommentPostAdmin(admin.ModelAdmin):
	list_display = ('article','nickname','email','date')

admin.site.register(Article,ArticlePostAdmin)
admin.site.register(Comment,CommentPostAdmin)
admin.site.register(Category)
admin.site.register(Tag)