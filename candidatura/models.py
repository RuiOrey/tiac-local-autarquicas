from django.db import models
from django.forms import ModelForm

class Distrito(models.Model):
	distrito= models.CharField(max_length=200)
	def __unicode__(self):
		return self.distrito

class Municipio(models.Model):
    municipio = models.CharField(max_length=200)
    distrito = models.ForeignKey(Distrito)
    def __unicode__(self):
        return self.municipio


class Partido(models.Model):
	nome_partido = models.CharField(max_length=200)
	foto = models.ImageField(upload_to='partidos')
	def __unicode__(self):
		return self.nome_partido


class Cabeca(models.Model):
    nome = models.CharField(max_length=200)
    foto = models.ImageField(upload_to='callable(object)', blank = True)
    numero_candidadaturas=models.DecimalField(max_digits=2, decimal_places=1)
    def __unicode__(self):
        return self.nome
    def limite_mandato(self):
    	return self.numero_candidadaturas > 3   

class Candidatura(models.Model):
    nome_candidatura = models.CharField(max_length=200,unique=True)
    municipio = models.ForeignKey(Municipio)
    partidos=models.ManyToManyField(Partido)
    candidato = models.ForeignKey(Cabeca,unique=True)
    def __unicode__(self):
		return self.nome_candidatura



class CandidaturaForm(ModelForm):
	class Meta:
		model=Candidatura