from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^process$', views.process),
    url(r'^processproduct$', views.processproduct),
    url(r'^likedproduct/(?P<id>\d+)$', views.likedproduct),
    url(r'^success$', views.success),
    url(r'^clear$', views.clear),
    url(r'^logout$', views.logout)
]
