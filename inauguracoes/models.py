from django.db import models
from django.forms import ModelForm
from candidatura.models import Candidatura

class Inauguracoes(models.Model):
	tipo		= models.CharField(max_length=300)
	foto		= models.ImageField(upload_to='denuncias')
	data		= models.DateTimeField(auto_now_add=True,editable=True)
	candidatura = models.ForeignKey(Candidatura)
	def __unicode__(self):
		return self.tipo

