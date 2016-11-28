from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^index', views.index, name='index'),
    url(r'^upload', views.upload, name='upload'),
    url(r'^init', views.init, name='init'),
]