from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$',views.index,name='index'),
	url(r'^(?P<article_id>[0-9]+)/',views.article,name='article'),
	url(r'^cat=(?P<category_id>[0-9]+)',views.category,name = 'category'),
	url(r'^tag=(?P<tag_id>[0-9]+)',views.tag,name = 'tag'),
	url(r'^allblogs',views.all,name='all blogs'),
	url(r'^cat',views.cat_menu,name='cat menu'),
	url(r'^about',views.about,name='about'),
]