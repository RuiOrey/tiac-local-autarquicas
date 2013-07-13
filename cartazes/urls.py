from django.conf.urls import patterns, url, include
from django.conf.urls.defaults import *
from tastypie.api import Api
from api import RegistoFotoResource, CandidaturaResource
from cartazes import views


registo_resource= RegistoFotoResource()

v1_api = Api(api_name='v1')
v1_api.register(RegistoFotoResource())
v1_api.register(CandidaturaResource())

urlpatterns= patterns('',
	url(r'^api/', include(v1_api.urls)),
)