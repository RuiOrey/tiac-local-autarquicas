from django.db import models
from django.forms import ModelForm



# Create your models here.

class Tipo(models.Model):
	tipo= models.CharField(max_length=300)
	def __unicode__(self):
		return self.tipo