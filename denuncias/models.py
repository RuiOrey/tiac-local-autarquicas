from django.db import models
from django.forms import ModelForm
from candidatura.models import Candidatura

class Tipo(models.Model):
	tipo		= models.CharField(max_length=300)
	def __unicode__(self):
		return self.tipo
		
class Denuncia(models.Model):
	ESTADO = (
		('1','Sob Revisao'),
		('2','Aprovada'),
		('3','Nao Aprovada'),
	)

	#depois tem de se inserir chave externa o user
	nome		= models.CharField(max_length=100)
	email		= models.EmailField(max_length=75, blank=True)
	data		= models.DateTimeField(auto_now_add=True,editable=True)
	descricao	= models.TextField(blank=True)
	estado		= models.CharField(max_length=1,choices=ESTADO, blank=True)
	candidatura = models.ForeignKey(Candidatura)
	tipo 		= models.ForeignKey(Tipo, blank=True)
	ficheiro	= models.FileField(upload_to='denuncias', blank=True)
	def __unicode__(self):
		return self.nome
