
from django.conf.urls import url
from form_basic import views
from django.conf.urls import include

urlpatterns = [
   url(r'^$', views.index, name='index'), 
   url(r'^reguser$', views.reguser, name='reguser'),  
   url(r'^statictest$', views.statictest, name='statictest'),
   url(r'^websiteadd$', views.websiteadd, name='websiteadd'),
   url(r'^testforloop$', views.testforloop, name='testforloop'),
]


