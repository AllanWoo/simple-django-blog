from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Articles(models.Model):
	title = models.CharField(max_length = 150)
	body = models.TextField()
	date = models.DateTimeField('date published')