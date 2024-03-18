from django.db import models
from datetime import datetime

# Create your models here.
class Post(models.Model):
	title= models.CharField(max_length=1000, default='')
	created_at= models.DateTimeField(default=datetime.now, blank= True)
	image = models.ImageField(upload_to='static/assets/img/', null=True, blank=True)
	section= models.CharField(max_length=100, default='')
	author= models.CharField(max_length=100, default='')
	body = models.TextField(default='')