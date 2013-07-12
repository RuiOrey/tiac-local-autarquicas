from django.conf.urls import patterns, url, include
from api import RegistoFotoResource
from cartazes import views

#http://127.0.0.1:8000/cartazes/api/cartazes/?format=json
# ou
#http://127.0.0.1:8000/cartazes/api/cartazes/?format=xml

registo_resource= RegistoFotoResource()

urlpatterns= patterns('',
	url(r'^api/', include(registo_resource.urls)),
)