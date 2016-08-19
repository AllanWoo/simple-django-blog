import datetime
from haystack import indexes
from blog.models import Article

class ArticleIndex(indexes.SearchIndex,indexes.Indexable):
	text = indexes.CharField(document=True,use_template=True)
	date = indexes.DateTimeField(model_attr='date')
	title = indexes.CharField(model_attr='title')

	def get_model(self):
		return Article
	def index_queryset(self, using=None):
		"""Used when the entire index for model is updated."""
		return self.get_model().objects.filter(date__lte=datetime.datetime.now())

			