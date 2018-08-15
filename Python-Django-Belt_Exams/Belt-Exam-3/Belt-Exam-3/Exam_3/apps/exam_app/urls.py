from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^dashboard$', views.dashboard),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^add$', views.add),
    url(r'^createitem$', views.createitem),
    url(r'^show/(?P<poster_id>\d+)$', views.show),
    url(r'^join/(?P<item_id>\d+)$', views.join),
    url(r'^remove/(?P<item_id>\d+)$', views.remove),
]