from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import loader
from .models import Article,Category,Tag,Comment

# Create your views here.

def index(request):
	latest_articles_list = Article.objects.order_by('-date')
	category_list = Category.objects.order_by('-name')
	template = loader.get_template('blogs/index.html')
	context = {
		'latest_articles_list' : latest_articles_list,
		'category_list' : category_list,
	}
	return render(request,'blogs/index.html',context)

def article(request,article_id):
	try:
		article = Article.objects.get(pk=article_id)
	except Article.DoesNotExist:
		raise Http404("Article does not exist")
	return render(request, 'blogs/article.html', {'article': article})

def category(request,category_id):
	cur_cat = Category.objects.get(pk = category_id)
	articles = Article.objects.filter(category = cur_cat)
	return render(request, 'blogs/category.html', {'articles': articles})
