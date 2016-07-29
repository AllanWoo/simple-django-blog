from django.contrib import admin
from .models import Articles
# Register your models here.

class ArticlePostAdmin(admin.ModelAdmin):
	list_display = ('title','date')

admin.site.register(Articles,ArticlePostAdmin)