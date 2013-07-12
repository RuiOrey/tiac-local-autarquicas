from django.db import models
from django.forms import ModelForm
from candidatura.models import Candidatura

class Tipo(models.Model):
	nome = models.CharField(max_length=200)
	def __unicode__(self):
		return self.nome


class Elemento(models.Model):
    nome = models.CharField(max_length=200)
    tipo = models.ForeignKey(Tipo)
    custo = models.DecimalField(max_digits=65,decimal_places=10)
    descricao = models.TextField(blank=True)
    dimensao_altura = models.IntegerField()
    dimensao_largura = models.IntegerField()
    def __unicode__(self):
        return self.nome


class Registofoto(models.Model):
	#depois tem de se inserir chave externa o user
	classificacao=models.ForeignKey(Elemento)
	candidatura = models.ForeignKey(Candidatura)
	titulo = models.CharField(max_length=200,blank=True)
	descricao = models.TextField(blank=True)
	mapa = models.URLField(blank=True)
	foto = models.ImageField(upload_to='partidos/%s' % candidatura,blank=True)
	hora = models.DateTimeField(auto_now_add=True,editable=True)
	def __unicode__(self):
		return 'foto%d' % self.pk
