from django.db import models

# Create your models here.
from django.utils import timezone

class Post(models.Model):
## models.Model 表明Post是一个Django模型，需要保存到数据库中
	author = models.ForeignKey('auth.User')
	## ForeignKey指向另一个模型的连接
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_data = models.DateTimeField(blank=True, null=True)
	published_data = models.DateTimeField(blank=True, null=True)
	
	def publish(self):
		self.published_data = timezone.now()
		self.save()
	
	def __str__(self):
		return self.title