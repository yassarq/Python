from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^process$', views.process),
    url(r'^processquote$', views.processquote),
    url(r'^likedquote/(?P<id>\d+)$', views.likedquote),
    url(r'^success$', views.success),
    url(r'^clear$', views.clear),
    url(r'^logout$', views.logout),
    url(r'^show/(?P<poster_id>\d+)$', views.show),
    url(r'^join/(?P<item_id>\d+)$', views.join),

]
