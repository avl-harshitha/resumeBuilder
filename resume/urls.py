from django.conf.urls import url
from . import views
# from django.contrib.auth.views import login

urlpatterns = [
url(r'^$', views.home, name='home'),
url(r'^create$', views.create, name='create'),
url(r'^template1$', views.template1, name='template1'),
url(r'^template2$', views.template2, name='template2'),
url(r'^template3$', views.template3, name='template3'),
]