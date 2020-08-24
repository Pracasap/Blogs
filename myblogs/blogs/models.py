from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.
class Blogs(models.Model):
	author		= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	title		= models.CharField(max_length=10000)
	body		= models.TextField()
	created		= models.DateTimeField(default=timezone.now)


	