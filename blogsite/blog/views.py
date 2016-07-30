from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import loader
from .models import Article

# Create your views here.

def index(request):
	latest_articles_list = Article.objects.order_by('-date')
	template = loader.get_template('blogs/index.html')
	context = {
		'latest_articles_list' : latest_articles_list,
	}
	return render(request,'blogs/index.html',context)

def article(request,article_id):
	try:
		article = Article.objects.get(pk=article_id)
	except Article.DoesNotExist:
		raise Http404("Article does not exist")
	return render(request, 'blogs/article.html', {'article': article})
