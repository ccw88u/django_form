
from django.conf.urls import url
from form_basic import views


urlpatterns = [
   url(r'^$', views.index, name='index'), 
   url(r'^reguser$', views.reguser, name='reguser'),  
   
]