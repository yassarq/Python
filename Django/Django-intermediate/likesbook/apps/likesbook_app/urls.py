from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^process$', views.process),
    url(r'^processbook$', views.processbook),
    url(r'^likedbook/(?P<id>\d+)$', views.likedbook),
    url(r'^success$', views.success),
    url(r'^clear$', views.clear),
    url(r'^logout$', views.logout)
]
