from django.db import models
from django.forms import ModelForm
from candidatura.models import Candidatura

class Tipo(models.Model):
	tipo		= models.CharField(max_length=300)
	def __unicode__(self):
		return self.tipo
		
class Denuncias(models.Model):
	ESTADO = (
		('1','Sob Revisao'),
		('2','Aprovada'),
		('3','Nao Aprovada'),
	)
	nome		= models.CharField(max_length=100)
	email		= models.EmailField(max_length=75, blank=True)
	data		= models.DateTimeField(auto_now_add=True,editable=True)
	descricao	= models.CharField(max_length=300)
	foto		= models.ImageField(upload_to='denuncias')
	estado		= models.CharField(max_length=1,choices=ESTADO)
	candidatura = models.ForeignKey(Candidatura)
	tipo 		= models.ForeignKey(Tipo)
	def __unicode__(self):
		return self.nome
