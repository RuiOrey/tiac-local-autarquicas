#ficheiro que vai ter a API TastyPie segundo este video : http://www.youtube.com/watch?v=FtREKCAWqBk
from tastypie.resources import ModelResource
from tastypie.constants import ALL
from tastypie import fields
from cartazes.models import Registofoto
from candidatura.models import Candidatura
from django.db import models

class CandidaturaResource(ModelResource):
    class Meta:
        queryset = Candidatura.objects.all()
        resource_name = 'candidatura'
        fields=['nome_candidatura']

#http://127.0.0.1:8000/cartazes/api/cartazes/?format=json
# ou
#http://127.0.0.1:8000/cartazes/api/cartazes/?format=xml

class RegistoFotoResource(ModelResource):
	#retorna os dados de candidatura definidos no CandidaturaResource
	candidatura = fields.ForeignKey(CandidaturaResource,'candidatura', full=True)
	class Meta:
		queryset = Registofoto.objects.all()
		resource_name = 'cartazes'
		filtering = {'titulo':ALL}
