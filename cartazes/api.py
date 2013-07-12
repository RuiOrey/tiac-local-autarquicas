#ficheiro que vai ter a API TastyPie segundo este video : http://www.youtube.com/watch?v=FtREKCAWqBk
from tastypie.resources import ModelResource
from tastypie.constants import ALL
from cartazes.models import Registofoto



#http://127.0.0.1:8000/cartazes/api/cartazes/?format=json
# ou
#http://127.0.0.1:8000/cartazes/api/cartazes/?format=xml

class RegistoFotoResource(ModelResource):
	class Meta:
		queryset = Registofoto.objects.all()
		resource_name = 'cartazes'
		filtering = {'titulo':ALL}